import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';


_launchURLBrowser() async {
  const url = 'https://www.geeksforgeeks.org/';
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}

  
_launchURLApp() async {
  const url = 'https://www.geeksforgeeks.org/';
  if (await canLaunch(url)) {
    await launch(url, forceSafariVC: true, forceWebView: true);
  } else {
    throw 'Could not launch $url';
  }
}

class Accounts extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    const title = 'Accounts';

    return MaterialApp(
      title: title,
      home: Scaffold(
        appBar: AppBar(
          title: const Text(title),
          actions: const <Widget>[
            // First button - decrement
            IconButton(
              icon: Icon(Icons.add), 
              onPressed: _launchURLBrowser,
              ),
          ],
        ),
        body: GridView.count(
          // Create a grid with 2 columns. If you change the scrollDirection to
          // horizontal, this produces 2 rows.
          crossAxisCount: 1,
          // Generate 100 widgets that display their index in the List.
          children: List.generate(100, (index) {
            return Center(
              child: Text(
                'Item $index',
                style: Theme.of(context).textTheme.bodyText1,
              ),
            );
          }),
        ),
      ),
    );
  }
}
