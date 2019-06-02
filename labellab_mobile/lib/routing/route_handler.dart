import 'package:flutter/material.dart';
import 'package:fluro/fluro.dart';
import 'package:labellab_mobile/screen/main_screen.dart';

var mainHandler = Handler(
    handlerFunc: (BuildContext context, Map<String, List<String>> params) {
  return MainScreen();
});
