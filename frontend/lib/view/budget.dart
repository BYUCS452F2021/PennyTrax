import 'package:flutter/material.dart';

class Budget extends StatefulWidget {
    const Budget({Key? key}) : super(key: key);
    @override
    _BudgetState createState() => _BudgetState();
}

class _BudgetState extends State<Budget> {
  @override
  Widget build(BuildContext context) {
    return Text(
        'Budget Page',
        style: const TextStyle(
          fontSize: 17,
          color: Colors.green,
        ),
      );
  }
}