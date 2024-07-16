import os
import sys
import pip
import subprocess
from qgis.core import QgsApplication



QgsApplication.setPrefixPath(os.getenv('QGIS_PREFIX_PATH', True))
qgs = QgsApplication([], False)
qgs.initQgis()



settings_dir_path = QgsApplication.qgisSettingsDirPath()
plugin_name = 'atdm_tool'
plugin_path = os.path.join(settings_dir_path, 'python', 'plugins', plugin_name)
requirements_file = 'requirements.txt'
req_absolute_path = os.path.join(plugin_path, requirements_file)



with open(req_absolute_path) as fp:
    list_of_packages = [pkg.strip() for pkg in fp.read().split('\n') if pkg.strip()]


for pkg_name in list_of_packages:
  subprocess.run(['pip', 'install', pkg_name])
  (OR)
  pip.main(['install', pkg_name])
    
# Exit QGIS
qgs.exitQgis()