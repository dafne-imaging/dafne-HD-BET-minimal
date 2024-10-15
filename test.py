import dicomUtils
from dicomUtils.ui.pyDicomView import ImageShow
from HD_BET_minimal import hd_bet
import matplotlib.pyplot as plt

INPUT_FOLDER = './test_images/image0001.dcm'

medical_volume, *_ = dicomUtils.medical_volume_from_path(INPUT_FOLDER)
spacing = medical_volume.pixel_spacing

print("Spacing:", spacing)
brain, mask = hd_bet(medical_volume.volume, spacing, mode="fast", device=0, progress_callback=lambda x, y: print(x, "/", y))

im = ImageShow(brain)
plt.show()