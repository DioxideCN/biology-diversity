from ninja import Router
from biology.apis.animal import router as animal_router
from biology.apis.animal_classification import router as animal_classification_router
from biology.apis.animal_knowledge import router as animal_knowledge_router
from biology.apis.botany import router as botany_router
from biology.apis.botany_classification import router as botany_classification_router
from biology.apis.botany_knowledge import router as botany_knowledge_router
from biology.apis.equipment import router as equipment_router
# from biology.apis.recognition import router as recognition_router
from biology.apis.RealTime_recognition import router as realtime_recognition_router
from biology.apis.Recognition_batch import router as Recognition_batch_router
# from biology.apis.area import router as area_router
from biology.apis.point import router as point_router
from biology.apis.area_manage import router as area_manage_router
from biology.apis.point_manage import router as point_manage_router
from biology.apis.upload import router as upload_router
from biology.apis.equipment_template import router as template_router
from biology.apis.warning import router as warning_router
from biology.apis.title import router as title_router

biology_router = Router()
biology_router.add_router('/', animal_router, tags=["Animal"])
biology_router.add_router('/', animal_classification_router, tags=["Animal_classification"])
biology_router.add_router('/', animal_knowledge_router, tags=["Animal_knowledge"])
biology_router.add_router('/', botany_router, tags=["Botany"])
biology_router.add_router('/', botany_classification_router, tags=["Botany_classification"])
biology_router.add_router('/', botany_knowledge_router, tags=["Botany_knowledge"])
biology_router.add_router('/', equipment_router, tags=["Equipment"])
# biology_router.add_router('/', recognition_router, tags=["Recognition"])
biology_router.add_router('/', realtime_recognition_router, tags=["RealTime_recognition"])
biology_router.add_router('/', Recognition_batch_router, tags=["Recognition_batch"])
# biology_router.add_router('/', area_router, tags=["Area"])
biology_router.add_router('/', point_router, tags=["Point"])
biology_router.add_router('/', area_manage_router, tags=["Area_manage"])
biology_router.add_router('/', point_manage_router, tags=["Point_manage"])
biology_router.add_router('/', upload_router, tags=["Upload"])
biology_router.add_router('/', template_router, tags=["EquipmentTemplate"])
biology_router.add_router('/', warning_router, tags=["Warning"])
biology_router.add_router('/', title_router, tags=["Title"])