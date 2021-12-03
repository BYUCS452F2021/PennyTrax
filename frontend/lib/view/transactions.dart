import 'package:flutter/material.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:intl/intl.dart';
import 'package:frontend/globals.dart' as globals;
import 'package:frontend/view/edit_transactions.dart';

import 'add_transaction.dart';
import 'login_page.dart';

class Transactions extends StatefulWidget {
  const Transactions({Key? key}) : super(key: key);
  @override
  _TransactionsState createState() => _TransactionsState();
}

class _TransactionsState extends State<Transactions> {
  final moneyFormat = new NumberFormat.simpleCurrency();

  @override
  void initState() {
    super.initState();
    fetchTransactions();
  }

  Future<void> fetchTransactions() async {
    ServerFacade.getTransactions(globals.authToken).then((value) {
      setState(() {
        globals.transactionData = value;
      });
    }, onError: (error) {
      print(error);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.logout),
          onPressed: () {
            globals.authToken = "";
            globals.accountData = [];
            globals.transactionData = [];
            print("User logged out!");
            Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => LoginPage()),
            );
          },
        ),
        title: const Text('Transactions'),
        actions: globals.accountData.isNotEmpty
            ? <Widget>[
                IconButton(
                  icon: const Icon(Icons.add),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const AddTransaction()),
                    );
                  },
                ),
              ]
            : null,
      ),
      body: Center(
        child: RefreshIndicator(
          child: ListView.builder(
            itemCount: globals.transactionData.length,
            itemBuilder: (context, index) {
              return transactionRow(globals.transactionData[index]);
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
      child: GestureDetector(
          child: Card(
              elevation: 2,
              child: Padding(
                  padding: const EdgeInsets.only(
                      left: 8, right: 8, top: 8, bottom: 8),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Column(
                        mainAxisAlignment: MainAxisAlignment.start,
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(transaction["merchant_name"] ?? "",
                              style: const TextStyle(fontSize: 19)),
                          if (transaction["merchant_name"] !=
                              transaction["description"])
                            // Only show the description if it's different than the merchant name
                            Text(
                              transaction["description"],
                              style: const TextStyle(
                                  fontSize: 13, fontStyle: FontStyle.italic),
                            ),
                          Text(
                            transaction["date"],
                            style: const TextStyle(fontSize: 13),
                          )
                        ],
                      ),
                      Text(moneyFormat.format(transaction["amount"]),
                          style: const TextStyle(fontSize: 21))
                    ],
                  ))),
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) =>
                      EditTransactions(transaction: transaction)),
            );
          }),
    );
  }
}
