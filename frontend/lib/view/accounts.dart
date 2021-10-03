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
      body: GridView.count(
        // Number of columns
        crossAxisCount: 1,
        // Generate list of widgets
        children: List.generate(100, (index) {
          return Center(
            child: Text(
              'Item $index',
              style: Theme.of(context).textTheme.bodyText1,
            ),
          );
        }),
      ),
    );
  }
}
