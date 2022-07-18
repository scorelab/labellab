import 'dart:async';

import 'package:dio/dio.dart';

import '../../../data/repository.dart';
import '../../../model/issue.dart';
import 'issue_details_state.dart';

class IssueDetailBloc {
  Repository _repository = Repository();

  String? projectId;
  String? issueId;

  Issue? _issue;
  bool _isLoading = false;

  IssueDetailBloc(this.projectId, this.issueId) {
    _loadIssue();
  }

  void refresh() {
    _loadIssue();
  }

  void _loadIssue() {
    // _selectedImages = [];
    if (_isLoading) return;
    _isLoading = true;
    _setState(IssueDetailState.loading(issue: _issue));
    _repository.getIssue(projectId, issueId).then((issue) {
      this._issue = issue;
      _setState(IssueDetailState.success(issue));
       _isLoading = false;
    }).catchError((err) {
      if (err is DioError) {
        _setState(IssueDetailState.error(err.message.toString(),
            issue: _issue));
      } else {
        _setState(IssueDetailState.error(err.toString(), issue: _issue));
      }
      _isLoading = false;
    });
  }

  _setState(IssueDetailState state) {
    if (!_stateController.isClosed) _stateController.add(state);
  }

  StreamController<IssueDetailState> _stateController =
      StreamController<IssueDetailState>();

  Stream<IssueDetailState> get state => _stateController.stream;

  void dispose() {
    _stateController.close();
  }
}