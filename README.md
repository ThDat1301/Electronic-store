# Electronic-store

1. Clone this project
2. Install requirements.txt (pip install -r requirements.txt)
3. Go to electronic-store/settings.py adjust information of DATABASE, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
3. Migrate model (py manage.py migrate)
4. Go to home_page/commands/updatemodels.py run it to initialize data 
5. Go to home_page/stripe-add-product.py run it to initialize data in Stripe
6. Running server by py manage.py runserver
 
