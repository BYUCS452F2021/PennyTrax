import 'package:flutter/material.dart';
import 'package:frontend/navigation.dart';
import 'package:frontend/view/login_page.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:uuid/uuid.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:frontend/globals.dart' as globals;

var uuid = const Uuid();

final firstNameController = TextEditingController();
final lastNameController = TextEditingController();
final emailController = TextEditingController();
final passwordController = TextEditingController();

class RegisterPage extends StatefulWidget {
  @override
  _RegisterPageState createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  @override
  Widget build(BuildContext context) {
    final logo = Padding(
      padding: EdgeInsets.all(30),
      child: Image.asset(
        'assets/PennyTraxLogo.png',
        fit: BoxFit.cover,
      ),
    );

    final inputFirstName = Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        decoration: InputDecoration(
            hintText: 'First name',
            fillColor: Colors.white,
            filled: true,
            contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
            border:
                OutlineInputBorder(borderRadius: BorderRadius.circular(50.0))),
        controller: firstNameController,
      ),
    );

    final inputLastName = Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        decoration: InputDecoration(
            hintText: 'Last name',
            fillColor: Colors.white,
            filled: true,
            contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
            border:
                OutlineInputBorder(borderRadius: BorderRadius.circular(50.0))),
        controller: lastNameController,
      ),
    );

    final inputEmail = Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        decoration: InputDecoration(
            hintText: 'Email',
            fillColor: Colors.white,
            filled: true,
            contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
            border:
                OutlineInputBorder(borderRadius: BorderRadius.circular(50.0))),
        controller: emailController,
      ),
    );

    final inputPassword = Padding(
      padding: EdgeInsets.only(bottom: 20),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        obscureText: true,
        decoration: InputDecoration(
            hintText: 'Password',
            fillColor: Colors.white,
            filled: true,
            contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
            border:
                OutlineInputBorder(borderRadius: BorderRadius.circular(50.0))),
        controller: passwordController,
      ),
    );

    final buttonRegister = Padding(
      padding: EdgeInsets.only(bottom: 5),
      child: ButtonTheme(
        height: 56,
        child: RaisedButton(
          child: Text('Register',
              style: TextStyle(color: Colors.white, fontSize: 20)),
          color: Colors.black87,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(50)),
          onPressed: registerUser,
        ),
      ),
    );

    final buttonLogin = FlatButton(
        child: Text(
          'Already have an account? Log in here',
          style: TextStyle(color: Colors.grey, fontSize: 16),
        ),
        onPressed: () {
          Navigator.pushReplacement(
            context,
            MaterialPageRoute(builder: (context) => LoginPage()),
          );
        });

    return SafeArea(
      child: Scaffold(
        body: Center(
          child: ListView(
            shrinkWrap: true,
            padding: EdgeInsets.symmetric(horizontal: 20),
            children: <Widget>[
              logo,
              inputFirstName,
              inputLastName,
              inputEmail,
              inputPassword,
              buttonRegister,
              buttonLogin
            ],
          ),
        ),
        backgroundColor: const Color(0xff3d4761),
      ),
    );
  }

  void registerUser() {
    String salt = uuid.v4();
    Map<String, String> register = {
      'first_name': firstNameController.text,
      'last_name': lastNameController.text,
      'email': emailController.text,
      'password': passwordController.text,
      'salt': salt,
    };

    ServerFacade.registerUser(register).then((response) {
      if (!response['success']) {
        print('Register was unsuccessful');
        Fluttertoast.showToast(
            msg: response['message'],
            toastLength: Toast.LENGTH_LONG,
            gravity: ToastGravity.CENTER,
            timeInSecForIosWeb: 3,
            backgroundColor: Colors.white,
            textColor: Colors.red,
            fontSize: 24.0,
            webBgColor: "#ffffff",
            webPosition: 'center');
      } else {
        print("User registered!");
        globals.authToken = response["auth_token"];
        firstNameController.text = "";
        lastNameController.text = "";
        emailController.text = "";
        passwordController.text = "";
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => AppNavigation()),
        );
      }
    }, onError: (error) {
      print(error);
    });
  }
}
