# https://www.kaggle.com/datasets/alvarobasily/road-damage

import glob
import os

import numpy as np
import supervisely as sly
from supervisely.io.fs import get_file_name, get_file_name_with_ext
from tqdm import tqdm


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/almaz/Downloads/RoadDamageDataset"
    ds_name = "ds0"
    batch_size = 30

    def _create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        ann_path = os.path.join(dataset_path, get_file_name(image_path) + ".txt")

        with open(ann_path) as f:
            content = f.read().split("\n")

        for curr_data in content:
            if len(curr_data) != 0:
                ann_data = list(map(float, curr_data.split(" ")))
                curr_obj_class = idx_to_obj_class[int(ann_data[0])]
                left = int((ann_data[1] - ann_data[3] / 2) * img_wight)
                right = int((ann_data[1] + ann_data[3] / 2) * img_wight)
                top = int((ann_data[2] - ann_data[4] / 2) * img_height)
                bottom = int((ann_data[2] + ann_data[4] / 2) * img_height)
                rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                label = sly.Label(rectangle, curr_obj_class)
                labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class_pothole = sly.ObjClass("pothole", sly.Rectangle)
    obj_class_alligator_crack = sly.ObjClass("alligator crack", sly.Rectangle)
    obj_class_longitudinal_crack = sly.ObjClass("longitudinal crack", sly.Rectangle)
    obj_class_lateral_crack = sly.ObjClass("lateral crack", sly.Rectangle)
    idx_to_obj_class = {
        0: obj_class_pothole,
        1: obj_class_alligator_crack,
        2: obj_class_longitudinal_crack,
        3: obj_class_lateral_crack,
    }
    obj_class_collection = sly.ObjClassCollection(
        [
            obj_class_pothole,
            obj_class_alligator_crack,
            obj_class_longitudinal_crack,
            obj_class_lateral_crack,
        ]
    )

    images_pathes = glob.glob(dataset_path + "/*.jpeg")

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = tqdm(total=len(images_pathes), desc="Create dataset {}".format(ds_name))

    for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
        images_names_batch = [get_file_name_with_ext(image_path) for image_path in img_pathes_batch]

        anns_batch = [_create_ann(image_path) for image_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(images_names_batch))

    return project
