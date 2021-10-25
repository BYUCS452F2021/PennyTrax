import 'package:flutter/material.dart';
import 'package:frontend/network/server_facade.dart';

class Transactions extends StatefulWidget {
    const Transactions({Key? key}) : super(key: key);
    @override
    _TransactionsState createState() => _TransactionsState();
}

class _TransactionsState extends State<Transactions> {

  List<dynamic> transactionData = [];

  @override
  void initState() {
    super.initState();
    fetchTransactions();
  }

  Future<void> fetchTransactions() async {
    List account_ids = ["G9mn4EDXGatApajnw6rnSdakjWX5mxf1DNn7a"];
    ServerFacade.getTransactions(account_ids).then((value) {
      setState(() {
        transactionData = value;
      });
    }, onError: (error) {
      print(error);
    });
  }

  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Appbar would go here
      body: Center(
        child: RefreshIndicator(
          child: ListView.builder(
            itemCount: transactionData.length,
            itemBuilder: (context, index) {
              return transactionRow(transactionData[index]);
            },
          ),
          onRefresh: fetchTransactions,
        ),
      ),
    );
  }
Widget transactionRow(transaction) {
    return Padding(
      padding: const EdgeInsets.only(left: 5, right: 10, top: 15),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            '${transaction["description"]}',
            style: const TextStyle(fontSize: 17),
          ),
          Text(
            '${transaction["merchant_name"]}',
            style: const TextStyle(fontSize: 15),
          ),
          Text(
            '${transaction["date"]} ${transaction["amount"]}',
            style: const TextStyle(fontSize: 13),
          )
        ],
      ),
    );
  }
}