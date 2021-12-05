import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:intl/intl.dart';
import 'package:frontend/globals.dart' as globals;
import 'add_edit_transaction.dart';

class ViewTransaction extends StatefulWidget {
  const ViewTransaction({Key? key, required this.transaction})
      : super(key: key);
  final dynamic transaction;

  @override
  _ViewTransactionState createState() => _ViewTransactionState();
}

class _ViewTransactionState extends State<ViewTransaction> {
  final moneyFormat = new NumberFormat.simpleCurrency();
  dynamic transaction;

  @override
  void initState() {
    super.initState();
    transaction = this.widget.transaction;
    print(transaction);
  }

  Future<void> loadTransaction() async {}

  void editTransaction() {
    Navigator.push(
      context,
      MaterialPageRoute(
          builder: (context) =>
              AddEditTransaction(transaction: transaction)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Transaction Details'),
        actions: globals.accountData.isNotEmpty
            ? <Widget>[
                IconButton(
                  icon: const Icon(Icons.delete),
                  onPressed: () {
                    ServerFacade.deleteTransaction(transaction["id"]).then(
                        (value) {
                      print("Transaction deleted!");
                      Navigator.pop(context);
                    }, onError: (error) {
                      print(error);
                    });
                  },
                ),
              ]
            : null,
      ),
      body: Center(
          child: Padding(
              padding: EdgeInsets.all(20),
              child: Column(children: [
                Text(moneyFormat.format(this.transaction["amount"]),
                    style: const TextStyle(fontSize: 25)),
                Text(this.transaction["description"],
                    style: const TextStyle(
                        fontSize: 18, fontStyle: FontStyle.italic)),
                Text(this.transaction["date"],
                    style: const TextStyle(fontSize: 18)),
                Text("(account)", style: const TextStyle(fontSize: 18)),
                infoRow("Merchant", this.transaction["merchant_name"] ?? ""),
                infoRow("Category", this.transaction["category"]),
                infoRow("Notes", this.transaction["notes"]),
                infoRow("Split Transaction", "", button: true),
                infoRow("Edit Transaction", "", button: true, action: editTransaction),
                Divider()
              ]))),
    );
  }

  Widget infoRow(displayName, value, {button = false, action = null}) {
    return Padding(
        padding: EdgeInsets.all(5),
        child:
            Row(mainAxisAlignment: MainAxisAlignment.spaceBetween, children: [
          Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Divider(),
            Text(displayName, style: const TextStyle(fontSize: 20)),
            Text(value,
                style:
                    const TextStyle(fontSize: 18, fontStyle: FontStyle.italic)),
          ]),
          if (button)
            IconButton(
                icon: const Icon(CupertinoIcons.chevron_right),
                onPressed: () {action();})
        ]));
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
                      ]),
                  Text(moneyFormat.format(transaction["amount"]),
                      style: const TextStyle(fontSize: 21))
                ],
              ))),
    );
  }
}
