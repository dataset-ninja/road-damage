Dataset **Road Damage** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwMzBfUm9hZCBEYW1hZ2Uvcm9hZC1kYW1hZ2UtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiOGpQQWZMa1BtT1lEVXF0L0xTK2swYUIvejljb3M5UC90YU5YY2crUWY1Yz0ifQ==)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Road Damage', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/alvarobasily/road-damage/download?datasetVersionNumber=1).