import 'package:flutter/material.dart';
import 'package:frontend/register_page.dart';
import 'package:frontend/model/login_request.dart';
import 'package:frontend/network/server_facade.dart';

//TODO: add controller

// ignore: use_key_in_widget_constructors
class LoginRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Simple Login Page',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LoginPage(),
    );
  }
}

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
      padding: EdgeInsets.all(20),
        child: Hero(
        tag: 'hero',
        child: CircleAvatar(
          radius: 100.0,
          child: Image.asset('assets/PennyTrax.png'),
        )
      ),
    );
    final inputEmail = Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        decoration: InputDecoration(
          hintText: 'Email',
          contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(50.0)
          )
        ),
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
          contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(50.0)
          )
        ),
        controller: passwordController,
      ),
    );
    final buttonLogin = Padding(
      padding: EdgeInsets.only(bottom: 5),
      child: ButtonTheme(
        height: 56,
        child: RaisedButton(
          child: Text('Login', style: TextStyle(color: Colors.white, fontSize: 20)),
          color: Colors.black87,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(50)
          ),
          onPressed: loginUser,
        ),
      ),
    );
    final buttonRegister = FlatButton(
      child: Text('Don\'t have an account? Register here', style: TextStyle(color: Colors.grey, fontSize: 16),),
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => RegisterRoute()),
        );
      }
    );
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
      )
    );
  }
  void loginUser() {
  Map<String, String> login = {
    'email': emailController.text,
    'password': passwordController.text
  };

  ServerFacade.addCashAccount(login).then((value) {
        print("User logged in");
      }, onError: (error) {
        print(error);
      });
  }
}



