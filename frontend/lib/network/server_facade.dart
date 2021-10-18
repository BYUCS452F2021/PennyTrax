import 'dart:async';
import 'dart:convert';

import 'package:frontend/model/institution_link_response.dart';
import 'package:frontend/model/register_request.dart';
import 'package:http/http.dart' as http;

class ServerFacade {
  static const String serverURL = "http://localhost:8000/";

  /*
  * Gets link url from server
  */
  static Future<InstitutionLinkResponse> addInstitution() async {
    final response = await http.post(Uri.parse(serverURL + 'institutions/add'));

    if (response.statusCode == 200) {
      return InstitutionLinkResponse.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to retrieve institution link response');
    }
  }

  /*
  * Registers user on the server
  */
  static Future<bool> registerUser() async {
    final response = await http.post(Uri.parse(serverURL + 'register/'));

    if (response == True) {
      return True;
    } else {
      throw Exception('Failed to register user');
    }
  }

  /*
  * Gets authtoken from server
  */
  static Future<LoginResponse> loginUser() async {
    final response = await http.post(Uri.parse(serverURL + 'login/'));

    if (response.statusCode == 200) {
      return LoginResponse.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to log in user');
    }
  }
}
