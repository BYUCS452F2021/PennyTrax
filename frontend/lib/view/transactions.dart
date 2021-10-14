import 'package:flutter/material.dart';

class Transactions extends StatefulWidget {
    const Transactions({Key? key}) : super(key: key);
    @override
    _TransactionsState createState() => _TransactionsState();
}

class _TransactionsState extends State<Transactions> {
  @override
  Widget build(BuildContext context) {
    return Text(
        'Transactions Page',
        style: const TextStyle(
          fontSize: 17,
          color: Colors.green,
        ),
      );
  }
}