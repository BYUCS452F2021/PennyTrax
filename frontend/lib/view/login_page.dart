import 'package:flutter/material.dart';
import 'package:frontend/view/register_page.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:frontend/navigation.dart';
import 'package:fluttertoast/fluttertoast.dart';

// ignore: use_key_in_widget_constructors

final emailController = TextEditingController();
final passwordController = TextEditingController();

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  @override
  Widget build(BuildContext context) {
    final logo = Padding(
      padding: EdgeInsets.all(30),
      child: Image.asset(
        'assets/PennyTraxLogo.png',
        fit: BoxFit.cover,
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
    final buttonLogin = Padding(
      padding: EdgeInsets.only(bottom: 5),
      child: ButtonTheme(
        height: 56,
        child: RaisedButton(
          child: Text('Login',
              style: TextStyle(color: Colors.white, fontSize: 20)),
          color: Colors.black87,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(50)),
          onPressed: () => loginUser(context),
        ),
      ),
    );
    final buttonRegister = FlatButton(
        child: Text(
          'Don\'t have an account? Register here',
          style: TextStyle(color: Colors.grey, fontSize: 16),
        ),
        onPressed: () {
          Navigator.pushReplacement(
            context,
            MaterialPageRoute(builder: (context) => RegisterPage()),
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
            inputEmail,
            inputPassword,
            buttonLogin,
            buttonRegister
          ],
        ),
      ),
      backgroundColor: const Color(0xff3d4761),
    ));
  }

  void loginUser(BuildContext context) {
    Map<String, String> login = {
      'email': emailController.text,
      'password': passwordController.text
    };

    ServerFacade.loginUser(login).then((response) {
      if (!response['success']) {
        print(response['message']);
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
        print("User logged in!");
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
