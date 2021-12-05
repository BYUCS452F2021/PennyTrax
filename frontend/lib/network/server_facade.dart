import 'dart:async';
import 'dart:convert';

import 'package:frontend/model/institution_link_response.dart';
import 'package:http/http.dart' as http;

class ServerFacade {
  static const String serverURL = "http://localhost:8000/";

  /*
  * Gets link url from server
  */
  static Future<InstitutionLinkResponse> addInstitution(Map body) async {
    final response = await http.post(
      Uri.parse(serverURL + 'institutions/add'),
      body: json.encode(body),
      headers: {
        'Content-type': 'application/json',
      },
    );

    if (response.statusCode == 200) {
      return InstitutionLinkResponse.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Failed to retrieve institution link response');
    }
  }

  /*
  * Registers user on the server
  */
  static Future<dynamic> registerUser(Map body) async {
    return await postRequest('register/', body);
  }

  /*
  * Gets authtoken from server
  */
  static Future<dynamic> loginUser(Map body) async {
    return await postRequest('login/', body);
  }

/* Get all of a users accounts account */
  static Future<dynamic> getAccounts(String authToken) async {
    var response =
        await http.get(Uri.parse(serverURL + 'accounts/' + authToken));
    return jsonDecode(response.body);
  }

  /* Create a new cash account */
  static Future<dynamic> addCashAccount(Map body) async {
    return await postRequest('accounts/add', body);
  }

  /* Get all of a users accounts account */
  static Future<dynamic> getTransactions(String authToken) async {
    Map body = {"authToken": authToken};
    // var response = await http.post(Uri.parse(serverURL + 'transactions'), body);
    var response = await postRequest('transactions', body);
    return response;
  }

  /* Add a transaction */
  static Future<dynamic> addTransaction(Map body) async {
    return await postRequest('transactions/add', body);
  }

  /* Add a transaction */
  static Future<dynamic> updateTransaction(Map body) async {
    return await postRequest('transactions/update', body);
  }

  /* Delete a transaction */
  static Future<dynamic> deleteTransaction(String transactionId) async {
    var response = await http
        .delete(Uri.parse(serverURL + 'transactions/delete/' + transactionId));
    return jsonDecode(response.body);
  }

  /* Create post request */
  static Future<dynamic> postRequest(String endpoint, Map body) async {
    return await http.post(
      Uri.parse(serverURL + endpoint),
      body: json.encode(body),
      headers: {
        'Content-type': 'application/json',
        //'Accept': 'application/json',
        //"Authorization": "Some token"
      },
    ).then((http.Response response) {
      final int statusCode = response.statusCode;
      if (statusCode < 200 || statusCode > 400 || json == null) {
        throw new Exception("Error while fetching data");
      }
      return json.decode(response.body);
    });
  }
}
