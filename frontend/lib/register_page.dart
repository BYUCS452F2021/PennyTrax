import 'package:flutter/material.dart';
import 'package:frontend/login_page.dart';
import 'package:frontend/main.dart';
import 'package:frontend/model/register_request.dart'
import 'package:frontend/network/server_facade.dart'
import 'package:uuid/uuid.dart';

//TODO: add controller

var uuid = Uuid();

class RegisterRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Simple Register Page',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: RegisterPage(),
    );
  }
}

class RegisterPage extends StatefulWidget {
  @override
  _RegisterPageState createState() => _RegisterPageState();
}
class _RegisterPageState extends State<RegisterPage> {
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
    final inputFirstName = Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        decoration: InputDecoration(
          hintText: 'First name',
          contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(50.0)
          )
        ),
      ),
    );
    final inputLastName = Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextField(
        keyboardType: TextInputType.emailAddress,
        decoration: InputDecoration(
          hintText: 'Last name',
          contentPadding: EdgeInsets.symmetric(horizontal: 25, vertical: 20),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(50.0)
          )
        ),
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
      ),
    );
    final buttonRegister = Padding(
      padding: EdgeInsets.only(bottom: 5),
      child: ButtonTheme(
        height: 56,
        child: RaisedButton(
          child: Text('Register', style: TextStyle(color: Colors.white, fontSize: 20)),
          color: Colors.black87,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(50)
          ),
          onPressed: () => {
            first_name = inputFirstName.Text
            last_name = inputLastName.Text
            email = inputEmail.Text
            password = inputPassword.Text
            salt = uuid.v4()
            register_request = RegisterRequest(first_name, last_name, email, password, salt)
            register_response = ServerFacade.registerUser(register_request)
          },
        ),
      ),
    );
    final buttonLogin = FlatButton(
      child: Text('Already have an account? Log in here', style: TextStyle(color: Colors.grey, fontSize: 16),),
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => LoginRoute()),
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
              inputFirstName,
              inputLastName,
              inputEmail,
              inputPassword,
              buttonRegister,
              buttonLogin
            ],
          ),
        ),
      )
    );
  }
}
