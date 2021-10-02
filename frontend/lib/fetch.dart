import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

Future<LinkResponse> fetchLinkURL() async {
  final response =
      await http.post(Uri.parse('http://localhost:8000/institutions/add'));

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return LinkResponse.fromJson(jsonDecode(response.body));
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

class LinkResponse {
  final String linkURL;

  LinkResponse({required this.linkURL});

  factory LinkResponse.fromJson(Map<String, dynamic> json) {
    return LinkResponse(
      linkURL: json['link_url'],
    );
  }
}

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late Future<LinkResponse> futureLinkResponse;

  @override
  void initState() {
    super.initState();
    futureLinkResponse = fetchLinkURL();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Fetch Data Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Fetch Data Example!'),
        ),
        body: Center(
          child: FutureBuilder<LinkResponse>(
            future: futureLinkResponse,
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                return Text(snapshot.data!.linkURL);
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}
