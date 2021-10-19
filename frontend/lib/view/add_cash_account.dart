import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'package:frontend/network/server_facade.dart';

class AddCashAccount extends StatefulWidget {
  const AddCashAccount({Key? key}) : super(key: key);

  @override
  _AddCashAccountState createState() => _AddCashAccountState();
}

class _AddCashAccountState extends State<AddCashAccount> {
  bool waitingForResonse = false;
  bool _autovalidate = false;
  final GlobalKey<FormState> _key = GlobalKey<FormState>();

  final accountNameController = TextEditingController();
  final initialBalanceController = TextEditingController();

  @override
  void initState() {
    super.initState();
    //futureLinkResponse = ServerFacade.addInstitution();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Cash Account'),
      ),
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
                  textDescription,
                  inputAccountName,
                  inputInitialBalance,
                  buttonCreateAccount,
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

  Widget get inputAccountName {
    return Padding(
      padding: EdgeInsets.only(bottom: 15),
      child: TextFormField(
        decoration: InputDecoration(labelText: 'Account Name'),
        validator: validateAccountName,
        controller: accountNameController,
      ),
    );
  }

  Widget get inputInitialBalance {
    return Padding(
      padding: EdgeInsets.only(bottom: 15),
      child: TextFormField(
        decoration: InputDecoration(
          labelText: 'Initial Balance',
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

  Widget get buttonCreateAccount {
    return Padding(
      padding: EdgeInsets.only(top: 25, bottom: 25),
      child: ButtonTheme(
        height: 40,
        child: RaisedButton(
          child: const Text('Create Account',
              style: TextStyle(color: Colors.white, fontSize: 15)),
          color: Colors.black87,
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(50)),
          onPressed: createAccount,
        ),
      ),
    );
  }

  Widget get loadingIndicator {
    return waitingForResonse ? const CircularProgressIndicator() : Container();
  }

  String? validateAccountName(String? input) {
    return input != null && input.trim().isNotEmpty
        ? null
        : "Please enter an account name";
  }

  String? validateInitialBalance(String? input) {
    return input != null && input.isNotEmpty
        ? null
        : "Please enter an initial balance";
  }

  void createAccount() {
    setState(() => {_autovalidate = true});
    if (_key.currentState!.validate()) {
      _key.currentState!.save();
      waitingForResonse = true;
      print("Creating cash account...");

      Map<String, String> account = {
        'name': accountNameController.text,
        'available_balance': initialBalanceController.text,
        'current_balance': initialBalanceController.text,
      };

      ServerFacade.addCashAccount(account).then((value) {
        print("Cash account created!");
        Navigator.pop(context);
      }, onError: (error) {
        print(error);
      });
    }
  }
}
