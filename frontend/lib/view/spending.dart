import 'package:flutter/material.dart';

class Spending extends StatefulWidget {
    const Spending({Key? key}) : super(key: key);
    @override
    _SpendingState createState() => _SpendingState();
}

class _SpendingState extends State<Spending> {
  @override
  Widget build(BuildContext context) {
    return Text(
        'Spending Page',
        style: const TextStyle(
          fontSize: 17,
          color: Colors.green,
        ),
      );
  }
}