import pyrebase

firebaseConfig = {
  apiKey: "AIzaSyDdyQrSu2DLkuFI-nR71m5hqN7LApoTJKI",
  authDomain: "bsi-2024.firebaseapp.com",
  projectId: "bsi-2024",
  storageBucket: "bsi-2024.appspot.com",
  messagingSenderId: "1067442231380",
  appId: "1:1067442231380:web:63e5c3243bde366859f5c1"
};

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

token = auth.sign_in_with_email_and_password("rafael.galafassi2005@gmail.com", "rafa1234!")

for k, v in auth.get_account_Info(token["idToken"]).items():
    print(k,v)
