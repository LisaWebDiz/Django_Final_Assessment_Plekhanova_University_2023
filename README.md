### Valencian Vacation: Plekhanov Uuniversity Final Assesment Diploma Django Project 2023
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
git clone https://github.com/yourusername/```bash
git clone https://github.com/yourusername/django_final_assessment_plekhanova_university.git
cd django_final_assessment_plekhanova_university

cp example.env .env
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=library
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432

```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Enjoy!git
cd ry_initial_django_project_2023

cp example.env .env
DEBUG=True
SECRET_KEY=your-secret-key
POSTGRES_DB=library
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432

```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Enjoy!

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


