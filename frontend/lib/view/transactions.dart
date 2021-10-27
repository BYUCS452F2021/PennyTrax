import 'package:flutter/material.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:intl/intl.dart';

class Transactions extends StatefulWidget {
  const Transactions({Key? key}) : super(key: key);
  @override
  _TransactionsState createState() => _TransactionsState();
}

class _TransactionsState extends State<Transactions> {
  final moneyFormat = new NumberFormat.simpleCurrency();
  List<dynamic> transactionData = [];

  @override
  void initState() {
    super.initState();
    fetchTransactions();
  }

  Future<void> fetchTransactions() async {
    List account_ids = ["G9mn4EDXGatApajnw6rnSdakjWX5mxf1DNn7a", "abc123"];
    // TODO: get these account_ids when the user logs in and store them somewhere globally accessible.
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
      appBar: AppBar(title: const Text('Transactions')),
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
      padding: const EdgeInsets.only(left: 5, right: 5),
      child: Card(
          elevation: 2,
          child: Padding(
              padding:
                  const EdgeInsets.only(left: 8, right: 8, top: 8, bottom: 8),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(transaction["merchant_name"],
                            style: const TextStyle(
                                fontSize: 19)),
                        if (transaction["merchant_name"] !=
                            transaction["description"])
                          // Only show the description if it's different than the merchant name
                          Text(
                            transaction["description"],
                            style: const TextStyle(fontSize: 13, fontStyle: FontStyle.italic),
                          ),
                        Text(
                          transaction["date"],
                          style: const TextStyle(fontSize: 13),
                        )
                      ]),
                  Text(moneyFormat.format(transaction["amount"]),
                      style: const TextStyle(fontSize: 21))
                ],
              ))),
    );
  }
}
