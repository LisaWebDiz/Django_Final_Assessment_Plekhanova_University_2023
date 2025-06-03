# Valencian Vacation: Plekhanov Uuniversity Final Assesment Diploma Django Project 2023
### Description
Web приложение для бронирования путешествия.  
Вывод списка объектов трех основных моделей и трех связанных с ними моделей.  
API основных моделей.  
Вывод каждого из объектов основных моделей и определенных полей, связанных с ними дополнительных моделей на отдельную страницу.  
Формы добавления, редактирования, обновления объектов трех основных моделей.  
Корзина, позволяющая бронировать объект на определенное количество дней.  
Тестирование приложения.  
Администрирование сайта.  
Фронтенд: CSS, Bootstrap  


### Quick start via Docker
```bash
git clone https://github.com/yourusername/django_final_assessment_plekhanova_university.git
cd django_final_assessment_plekhanova_university
cp example.env .env
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
Enjoy!

### API Documentation
    • Swagger: http://localhost:8000/swagger/
    • Redoc: http://localhost:8000/redoc/

### Features
    • Django admin panel for managing data
    • Fully documented REST API
    • Data storage using PostgreSQL
    • pgAdmin for database viewing: http://localhost:5050
    • Admin panel: http://localhost:8000/admin/
    • Registration/Authentication

### Pages
![Mainpage](assets/mainpage.png)
![Registration](assets/registration.png)
![Authentication](assets/auth.png)
![Villas_Catalogue](assets/villas.png)
![Yachts_Catalogue](assets/yachts.png)
![Vehicles_Catalogue](assets/vehicles.png)
![Villa_Detail](assets/villa_detail.png)
![Yacht_Detail](assets/yacht_detail.png)
![Vehicle_Detail](assets/vehicle_detail.png)
![Your_Booking](assets/booking.png)
![Add_Yacht](assets/yacht_add.png)
![Update_Villa](assets/villa_update.png)
![Contact us](assets/contact_us.png)
