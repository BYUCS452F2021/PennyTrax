import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:intl/intl.dart';
import 'package:frontend/globals.dart' as globals;

class AddTransaction extends StatefulWidget {
  const AddTransaction({Key? key}) : super(key: key);
  @override
  _AddTransactionState createState() => _AddTransactionState();
}

class _AddTransactionState extends State<AddTransaction> {
  final moneyFormat = new NumberFormat.simpleCurrency();
  dynamic transaction;

  bool waitingForResonse = false;
  bool _autovalidate = false;
  final GlobalKey<FormState> _key = GlobalKey<FormState>();

  final accountNameController = TextEditingController();
  final dateController = TextEditingController();
  final initialBalanceController = TextEditingController();
  final merchantNameController = TextEditingController();
  final descriptionController = TextEditingController();
  final notesController = TextEditingController();

  String dropdownValue = 'One';

  @override
  void initState() {
    dateController.text = DateTime.now().toString().substring(0, 10);
    super.initState();
  }

  Future<void> loadTransaction() async {}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Add Transaction')),
      body: Center(
        child: Form(
          key: _key,
          autovalidate: _autovalidate,
          child: Padding(
            padding: const EdgeInsets.all(15),
            child: Container(
              alignment: Alignment.center,
              child: Column(
                children: <Widget>[
                  inputAccount,
                  inputDate,
                  inputAmount,
                  inputTextField("Merchant Name", merchantNameController),
                  inputTextField("Description", descriptionController),
                  inputTextField("Notes", notesController),
                  buttonAddTransaction,
                  loadingIndicator,
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget get textDescription {
    return const Padding(
      padding: EdgeInsets.only(top: 50, bottom: 50),
      child: Text(
        "A cash account allows you to keep track of cash you have or an account you have that isn't in under a supported institution.",
        textAlign: TextAlign.center,
      ),
    );
  }

  Widget get inputAccount {
    return Padding(
      padding: EdgeInsets.only(bottom: 15),
      child: InputDecorator(
        decoration: InputDecoration(
          labelText: 'Account',
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(5.0)),
          contentPadding: EdgeInsets.all(10),
        ),
        child: DropdownButton<String>(
          value: dropdownValue,
          icon: const Icon(Icons.arrow_downward),
          hint: const Text("Account"),
          iconSize: 24,
          elevation: 16,
          isExpanded: true,
          onChanged: (String? newValue) {
            setState(() {
              dropdownValue = newValue!;
            });
          },
          items: <String>['One', 'Two', 'Free', 'Four']
              .map<DropdownMenuItem<String>>((String value) {
            return DropdownMenuItem<String>(
              value: value,
              child: Text(value),
            );
          }).toList(),
        ),
      ),
    );
  }

  Widget inputTextField(label, controller) {
    return Padding(
      padding: EdgeInsets.only(bottom: 15),
      child: TextFormField(
        decoration: InputDecoration(labelText: label),
        controller: controller,
      ),
    );
  }

  Widget get inputAmount {
    return Padding(
      padding: EdgeInsets.only(bottom: 15),
      child: TextFormField(
        decoration: const InputDecoration(
          labelText: 'Amount',
          prefixText: '\$ ',
        ),
        inputFormatters: [
          WhitelistingTextInputFormatter(RegExp(r"^\d+\.?\d{0,2}"))
        ],
        validator: validateInitialBalance,
        controller: initialBalanceController,
      ),
    );
  }

  Widget get inputDate {
    return Padding(
      padding: EdgeInsets.only(bottom: 15),
      child: TextField(
        controller: dateController, //editing controller of this TextField
        decoration: const InputDecoration(
          labelText: "Date",
          suffixIcon: Icon(Icons.calendar_today),
        ),
        readOnly: true, //set it true, so that user will not able to edit text
        onTap: () async {
          DateTime? pickedDate = await showDatePicker(
            context: context,
            initialDate: DateTime.parse(dateController.text),
            firstDate: DateTime(
                2000), //DateTime.now() - not to allow to choose before today.
            lastDate: DateTime(2101),
          );
        },
      ),
    );
  }

  Widget get buttonAddTransaction {
    return Padding(
      padding: EdgeInsets.only(top: 25, bottom: 25),
      child: ButtonTheme(
        height: 40,
        child: RaisedButton(
          child: const Text('Add Transaction',
              style: TextStyle(color: Colors.white, fontSize: 15)),
          color: Colors.black87,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(50)),
          onPressed: addTransaction,
        ),
      ),
    );
  }

  Widget get loadingIndicator {
    return waitingForResonse ? const CircularProgressIndicator() : Container();
  }

  String? validateTextField(String? input) {
    return input != null && input.trim().isNotEmpty
        ? null
        : "Please enter an input";
  }

  String? validateInitialBalance(String? input) {
    return input != null && input.isNotEmpty
        ? null
        : "Please enter an initial balance";
  }

  void addTransaction() {
    setState(() => {_autovalidate = true});
    if (_key.currentState!.validate()) {
      _key.currentState!.save();
      waitingForResonse = true;
      print("Adding transaction...");

      // Map<String, String> account = {
      //   'authToken': globals.authToken,
      //   'name': accountNameController.text,
      //   'available_balance': initialBalanceController.text,
      //   'current_balance': initialBalanceController.text,
      // };

      // ServerFacade.addCashAccount(account).then((value) {
      //   print("Cash account created!");
      //   Navigator.pop(context);
      // }, onError: (error) {
      //   print(error);
      // });
    }
  }
}
