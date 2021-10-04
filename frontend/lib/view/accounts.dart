import 'package:flutter/material.dart';
import 'package:frontend/model/institution_link_response.dart';
import 'package:frontend/view/add_institution.dart';

class Accounts extends StatefulWidget {
  const Accounts({Key? key}) : super(key: key);

  @override
  _AccountsState createState() => _AccountsState();
}

class _AccountsState extends State<Accounts> {
  late Future<InstitutionLinkResponse> futureLinkResponse;

  @override
  void initState() {
    super.initState();
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
      body: ListView.builder(
        itemCount: 3,
        itemBuilder: (context, index) {
          return accountCard(index);
        },
      ),
    );
  }
}

Widget accountCard(index) {
  return Container(
    padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
    height: 180,
    width: double.maxFinite,
    child: Card(
      elevation: 7,
      child: Padding(
        padding: EdgeInsets.all(7),
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
                            padding: EdgeInsets.only(left: 15, top: 5),
                            child: Align(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                'Your Bank ${index + 1}',
                                style: TextStyle(fontSize: 25),
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
                      Row(
                        children: const <Widget>[
                          Padding(
                            padding: EdgeInsets.only(left: 15, top: 15),
                            child: Align(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                "Savings (...8629)",
                                style: TextStyle(fontSize: 17),
                              ),
                            ),
                          ),
                          Padding(
                            padding: EdgeInsets.only(left: 100, top: 15),
                            child: Align(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                "\$ 7,231.34",
                                style: TextStyle(
                                    fontSize: 17, color: Colors.green),
                              ),
                            ),
                          )
                        ],
                      ),
                      Row(
                        children: const <Widget>[
                          Padding(
                            padding: EdgeInsets.only(left: 15, top: 15),
                            child: Align(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                "Checking (...3291)",
                                style: TextStyle(fontSize: 17),
                              ),
                            ),
                          ),
                          Padding(
                            padding: EdgeInsets.only(left: 100, top: 15),
                            child: Align(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                "\$ 2,421.16",
                                style: TextStyle(
                                    fontSize: 17, color: Colors.green),
                              ),
                            ),
                          )
                        ],
                      )
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
