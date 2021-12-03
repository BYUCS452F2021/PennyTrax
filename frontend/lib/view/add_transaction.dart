import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:intl/intl.dart';
import 'package:frontend/globals.dart' as globals;
import 'package:uuid/uuid.dart';

class AddTransaction extends StatefulWidget {
  const AddTransaction({Key? key}) : super(key: key);
  @override
  _AddTransactionState createState() => _AddTransactionState();
}

class _AddTransactionState extends State<AddTransaction> {
  bool waitingForResonse = false;
  bool _autovalidate = false;
  final GlobalKey<FormState> _key = GlobalKey<FormState>();

  final accountNameController = TextEditingController();
  final dateController = TextEditingController();
  final amountController = TextEditingController();
  final merchantNameController = TextEditingController();
  final descriptionController = TextEditingController();
  final categoryController = TextEditingController();
  final notesController = TextEditingController();

  String accountValue = '';
  List<dynamic> accounts = [];

  @override
  void initState() {
    super.initState();
    dateController.text = DateTime.now().toString().substring(0, 10);

    // Get list of accounts for dropdown
    globals.accountData.forEach((institution) {
      institution["accounts"].forEach((account) {
        accounts.add({
          "name": account["name"],
          "id": account["id"],
        });
      });
    });

    if (accounts.isNotEmpty) {
      accountValue = accounts.elementAt(0)["id"];
    }
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
                  inputTextField("Category", categoryController),
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
          value: accountValue,
          icon: const Icon(Icons.arrow_downward),
          hint: const Text("Account"),
          iconSize: 24,
          elevation: 16,
          isExpanded: true,
          onChanged: (String? newValue) {
            setState(() {
              accountValue = newValue!;
            });
          },
          items: accounts.map<DropdownMenuItem<String>>((account) {
            return DropdownMenuItem<String>(
              value: account["id"],
              child: Text(account["name"]),
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
        validator: validateAmount,
        controller: amountController,
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
          if (pickedDate != null) {
            //pickedDate output format => 2021-03-10 00:00:00.000
            String formattedDate = DateFormat('yyyy-MM-dd').format(pickedDate);
            setState(() {
              dateController.text = formattedDate;
            });
          }
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

  String? validateAmount(String? input) {
    return input != null && input.isNotEmpty ? null : "Please enter an amount";
  }

  void addTransaction() {
    setState(() => {_autovalidate = true});
    if (_key.currentState!.validate()) {
      _key.currentState!.save();
      waitingForResonse = true;
      print("Adding transaction...");

      Map<String, String> transaction = {
        'id': Uuid().v4(),
        'account_id': accountValue,
        'date': dateController.text,
        'amount': amountController.text,
        'pending': "0",
        'merchant_name': merchantNameController.text,
        'description': descriptionController.text,
        'category': categoryController.text,
        'notes': notesController.text,
        'split': "0",
        'parent_transaction_id': "null",
        'hidden_from_budget': "0",
      };

      ServerFacade.addTransaction(transaction).then((value) {
        print("Transaction added!");
        Navigator.pop(context);
      }, onError: (error) {
        print(error);
      });
    }
  }
}
