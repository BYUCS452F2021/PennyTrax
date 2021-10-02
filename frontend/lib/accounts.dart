import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;

Future<http.Response> fetchAlbum() {
  return http.post(Uri.parse('https://localhost:8000/institutions/add/'));
}


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
            IconButton(
              icon: Icon(Icons.add), 
              onPressed: _launchURLBrowser,
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
      ),
    );
  }
}
