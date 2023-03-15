import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'electronic-store.settings'
application = get_wsgi_application()

from home_page.models import Category, Product


def create_category():
    Category.objects.update_or_create(name="Laptops & Computers",
                                      image='home_page/images/collection/laptops-computers_300x.avif')
    Category.objects.update_or_create(name="Cameras",
                                      image='home_page/images/collection/camera.avif')
    Category.objects.update_or_create(name="Home Entertainment",
                                      image='home_page/images/collection/entertainment_300x.avif')
    Category.objects.update_or_create(name="Home Appliances",
                                      image='home_page/images/collection/home-appliance_300x.avif')
    Category.objects.update_or_create(name="Health & Beauty",
                                      image='home_page/images/collection/health-beauty_300x.avif')


def create_product():
    camera_category = Category.objects.get(name='Cameras')
    Product.objects.update_or_create(name='Alpha ILCE-6000L 24.3 MP Mirrorless',
                                     image='products/2023/02/ATX-NX100_24_MP Camcorder.webp',
                                     price='400',
                                     category=camera_category)
    Product.objects.update_or_create(name='Coolpix (A100) 20 MP Point & Shoot Camera',
                                     image='products/2023/02/Coolpix_(A100)_20 MP_Point&ShootCamera.webp',
                                     price='370',
                                     category=camera_category)
    Product.objects.update_or_create(name='Alpha ILCE-6000L 24.3 MP Mirrorless',
                                     image='products/2023/02/Coupon_Inside_Acer_DLP_3D_Projector.avif',
                                     price='329',
                                     category=camera_category)
    Product.objects.update_or_create(name='DSC-WX220 22.5 MP Cyber Shot Camera',
                                     image='products/2023/02/DSC-WX220_22.5_MP_Cyber_Shot_Camera.avif',
                                     price='600',
                                     category=camera_category)
    Product.objects.update_or_create(name='Samsung 9.8GLS',
                                     image='products/2023/02/Samsung9.8GLS.avif',
                                     price='400',
                                     category=camera_category)
    lapcom_category = Category.objects.get(name='Laptops & Computers')
    Product.objects.update_or_create(name='Acer NX.MVMSI.035 Intel Core i3 15.6 inches Laptop',
                                     image='products/2023/02/Acer NX.MVMSI.035_Intel_Core_i3_15.6_inches_Laptop.avif',
                                     price='1600',
                                     category=lapcom_category)
    Product.objects.update_or_create(name='Apple MB110LL/B Standard Keyboard Silver',
                                     image='products/2023/02/keaboard-1.2_180x.avif',
                                     price='50',
                                     category=lapcom_category)
    Product.objects.update_or_create(name='Acer Predator Intel Core i7',
                                     image='products/2023/02/Acer_Predator_Intel_Core_i7.avif',
                                     price='1000',
                                     category=lapcom_category)
    Product.objects.update_or_create(name='Laptop E40-80 80HR006RIH Intel Core i5',
                                     image='products/2023/02/Laptop_E40-80_80HR006RIH_Intel_Core_i5.avif',
                                     price='549',
                                     category=lapcom_category)
    Product.objects.update_or_create(name='SONY 8 GB USB Flash Drive (USM8M1)',
                                     image='products/2023/02/pendrive_180x.avif',
                                     price='20',
                                     category=lapcom_category)
    Product.objects.update_or_create(name='HOT PICK HP ENVY D052TU INTEL CORE I5 (6TH GENERATION) 13.3',
                                     image='products/2023/02/HOT_PICK_HP_ENVY_D052TU_INTEL_CORE_I5_(6TH_GENERATION).webp',
                                     price='700',
                                     category=lapcom_category)

    home_entertain_category = Category.objects.get(name='Home Entertainment')
    Product.objects.update_or_create(name='5.1 Channel Blu Ray Dollby Sound',
                                     image='products/2023/02/5.1_Channel_Blu_Ray_Dollby_Sound.avif',
                                     price='1700',
                                     category=home_entertain_category)
    Product.objects.update_or_create(name='Sony 32J4100 50 inches HD Ready LED',
                                     image='products/2023/02/Sony_32J4100_50_inches_HD_Ready_LED.avif',
                                     price='1200',
                                     category=home_entertain_category)
    Product.objects.update_or_create(name='Dualshock 3 PS3 Wireless Controller',
                                     image='products/2023/02/Dualshock_3_PS3_Wireless_Controller.avif',
                                     price='200',
                                     category=home_entertain_category)
    Product.objects.update_or_create(name='PS4 500 GB Gaming Console',
                                     image='products/2023/02/PS4_500_GB_Gaming_Console.avif',
                                     price='310',
                                     category=home_entertain_category)
    Product.objects.update_or_create(name='Musical Keyboard',
                                     image='products/2023/02/Musical_Keyboard.avif',
                                     price='100',
                                     category=home_entertain_category)
    home_appliances_category = Category.objects.get(name='Home Appliances')
    Product.objects.update_or_create(name='Fully Automatic Washing Machine',
                                     image='products/2023/02/Fully_Automatic_Washing_Machine.avif',
                                     price='600',
                                     category=home_appliances_category)
    Product.objects.update_or_create(name='GT Sonic VGT 800 Ultrasonic Cleaner',
                                     image='products/2023/02/GT_Sonic_VGT_800_Ultrasonic_Cleaner.avif',
                                     price='50',
                                     category=home_appliances_category)
    Product.objects.update_or_create(name='Haier Refrigerator Brushline Silver',
                                     image='products/2023/02/Haier_Refrigerator_Brushline_Silver.webp',
                                     price='600',
                                     category=home_appliances_category)
    Product.objects.update_or_create(name='1.5 Ton 3 Star Split AC',
                                     image='products/2023/02/1.5_Ton_3_Star_Split_AC.webp',
                                     price='1200',
                                     category=home_appliances_category)
    Product.objects.update_or_create(name='Samsung Automatic Washing Machine',
                                     image='products/2023/02/Samsung_Automatic_Washing_Machine.avif',
                                     price='1439',
                                     category=home_appliances_category)
    health_beauty_category = Category.objects.get(name='Health & Beauty')
    Product.objects.update_or_create(name='WAHL 5604-100 Men Trimmer (Black)',
                                     image='products/2023/02/WAHL_5604-100_Men_Trimmer.avif',
                                     price='8',
                                     category=health_beauty_category)
    Product.objects.update_or_create(name='Men, Women Hair Dryer',
                                     image='products/2023/02/Men_Women_Hair_Dryer.avif',
                                     price='5',
                                     category=health_beauty_category)
    Product.objects.update_or_create(name='JSB HF01 Swing Walker Massager (White & Blue)',
                                     image='products/2023/02/JSB_HF01_Swing_Walker_Massager.avif',
                                     price='120',
                                     category=health_beauty_category)
    Product.objects.update_or_create(name='Pack Women Hair Straightener & Dryer',
                                     image='products/2023/02/Pack_Women_Hair_Straightener_Dryer.avif',
                                     price='89',
                                     category=health_beauty_category)
    Product.objects.update_or_create(name='Philips HP6419/02 Women Epilator',
                                     image='products/2023/02/Philips_HP6419_02_Women_Epilator.avif',
                                     price='29',
                                     category=health_beauty_category)


if __name__ == '__main__':
    create_category()
    create_product()






