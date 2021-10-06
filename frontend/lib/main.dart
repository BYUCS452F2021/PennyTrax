import 'package:flutter/material.dart';
import 'package:frontend/view/accounts.dart';

void main() {
  runApp(MaterialApp(
    title: 'PennyTrax',
    home: const Accounts(),
    theme: ThemeData(
      primarySwatch: Colors.blue,
    ),
    debugShowCheckedModeBanner: false,
  ));
}
