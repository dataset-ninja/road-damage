Dataset **Road Damage** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/u/z/wx/QeUaB05Hom7rcF7U6xCWKay9kkL1Y2lE3rANgwXzSGJddvvJoOX4LP3rakhpxSTEJywO93AKhg60bisu7aSHKINwDjjYvpxEWHYcI2wPzbkJ2J26YgT4thoBHuyz.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Road Damage', dst_path='~/dtools/datasets/Road Damage.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/alvarobasily/road-damage/download?datasetVersionNumber=1)