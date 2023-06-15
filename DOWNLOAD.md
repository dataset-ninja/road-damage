Dataset **Road Damage** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/p/n/Hj/tEFqnSFoMr0ZefBal82EBhxzm1uJUT5Hv7smtjJ0cgoYVuKyHmgbcWqJqU1Ft4IlnGnT3OUDbvYC3SyY9nY6EQJTXhSFMFc4NoJougj11CldJJh0OCxdLMg40Qxz.tar)

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