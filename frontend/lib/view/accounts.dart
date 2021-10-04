import 'package:flutter/material.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:frontend/view/add_institution.dart';

class Accounts extends StatefulWidget {
  const Accounts({Key? key}) : super(key: key);

  @override
  _AccountsState createState() => _AccountsState();
}

class _AccountsState extends State<Accounts> {
  late Future<dynamic> futureGetAccountsResponse = ServerFacade.getAccounts();

  @override
  void initState() {
    super.initState();
    futureGetAccountsResponse = ServerFacade.getAccounts();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Accounts'),
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const AddInstitution()),
              );
            },
          ),
        ],
      ),
      body: Center(
        child: FutureBuilder<dynamic>(
          future: futureGetAccountsResponse,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return ListView.builder(
                itemCount: snapshot.data.length,
                itemBuilder: (context, index) {
                  return institutionCard(snapshot.data[index]);
                },
              );
            } else if (snapshot.hasError) {
              return Text('${snapshot.error}');
            }
            // By default, show a loading spinner.
            return const CircularProgressIndicator();
          },
        ),
      ),
    );
  }
}

Container institutionCard(institution) {
  return Container(
    padding: const EdgeInsets.fromLTRB(10, 10, 10, 0),
    height: (110 + (institution["accounts"].length * 35)).toDouble(),
    width: double.maxFinite,
    child: Card(
      elevation: 7,
      child: Padding(
        padding: const EdgeInsets.all(7),
        child: Stack(children: <Widget>[
          Align(
            alignment: Alignment.centerRight,
            child: Stack(
              children: <Widget>[
                Padding(
                  padding: const EdgeInsets.only(left: 10, top: 5),
                  child: Column(
                    children: <Widget>[
                      Row(
                        children: <Widget>[
                          Padding(
                            padding: const EdgeInsets.only(left: 15, top: 5),
                            child: Align(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                '${institution["financial_institution_name"]}',
                                style: const TextStyle(fontSize: 25),
                              ),
                            ),
                          )
                        ],
                      ),
                      Row(
                        children: const <Widget>[
                          Expanded(child: Divider()),
                        ],
                      ),
                      for (var account in institution["accounts"])
                        accountRow(account)
                    ],
                  ),
                )
              ],
            ),
          )
        ]),
      ),
    ),
  );
}

Widget accountRow(account) {
  return Padding(
    padding: const EdgeInsets.only(left: 5, right: 10, top: 15),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(
          '${account["name"]} (...${account["mask"]})',
          style: const TextStyle(fontSize: 17),
        ),
        accountAmount(account),
      ],
    ),
  );
}

Widget accountAmount(account) {
  if (account["type"] == "loan") {
    return Text(
      '- \$ ${account["current_balance"]}',
      style: const TextStyle(
        fontSize: 17,
        color: Colors.red,
      ),
    );
  } else {
    return Text(
      '\$ ${account["current_balance"]}',
      style: const TextStyle(
        fontSize: 17,
        color: Colors.green,
      ),
    );
  }
}
