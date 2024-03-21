import getpass
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
db = firebase.dataBase()

username = input("Digite o seu usuario: ")
password = getpass.getpass("Digite sua senha: ")

token = auth.sign_in_with_email_and_password("username", "password")

#print(token)


try:
    token = auth.sign_in_with_email_and_password(username,password)
except Exception as e:
    print(e)
    print("Login ou senha inválida")