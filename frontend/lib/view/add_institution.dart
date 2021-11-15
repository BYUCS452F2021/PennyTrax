import 'dart:async';

import 'package:flutter/material.dart';
import 'package:frontend/model/institution_link_response.dart';
import 'package:frontend/network/server_facade.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:frontend/globals.dart' as globals;

_launchURLBrowser(url) async {
  if (await canLaunch(url)) {
    await launch(url, forceWebView: true);
  } else {
    throw 'Could not launch $url';
  }
}

class AddInstitution extends StatefulWidget {
  const AddInstitution({Key? key}) : super(key: key);

  @override
  _AddInstitutionState createState() => _AddInstitutionState();
}

class _AddInstitutionState extends State<AddInstitution> {
  late Future<InstitutionLinkResponse> futureLinkResponse;

  @override
  void initState() {
    super.initState();
    Map body = {"authToken": globals.authToken};
    futureLinkResponse = ServerFacade.addInstitution(body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Institution'),
      ),
      body: Center(
        child: FutureBuilder<InstitutionLinkResponse>(
          future: futureLinkResponse,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              _launchURLBrowser("http://" + snapshot.data!.linkURL);
              Navigator.pop(context);
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
