import 'package:flutter/material.dart';
import 'package:frontend/view/login_page.dart';
import 'package:frontend/navigation.dart';

void main() {
  runApp(MaterialApp(
    title: 'Penny Trax',
    home: LoginPage(),
    theme: ThemeData(
      primarySwatch: Colors.blue,
    ),
    debugShowCheckedModeBanner: false,
  ));
}
