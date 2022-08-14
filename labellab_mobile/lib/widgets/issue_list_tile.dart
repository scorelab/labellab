import 'package:flutter/material.dart';
import 'package:labellab_mobile/model/mapper/issue_mapper.dart';
import '../model/issue.dart';

class IssueListTile extends StatelessWidget {
  final Issue issue;
  final bool isCustomized;
  final VoidCallback? onItemTapped;

  IssueListTile(this.issue, {this.onItemTapped, this.isCustomized = false});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: this.onItemTapped,
      child: Card(
        child: Container(
          height: 80,
          color: Colors.white,
          child: Row(
            children: [
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(6.0),
                  child: Container(
                    alignment: Alignment.topLeft,
                    child: Column(
                      children: [
                        Expanded(
                            flex: 4,
                            child: Row(
                              children: [
                                Text("#" + issue.id!.toString() + " ",
                                    style: TextStyle(
                                        fontSize: 20, color: Colors.grey)),
                                Text(issue.issueTitle!,
                                    style: TextStyle(
                                      fontSize: 16,
                                      fontWeight: FontWeight.bold,
                                    )),
                              ],
                            )),
                        Padding(
                          padding: const EdgeInsets.all(3.0),
                          child: Row(
                            // mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              coloredBox(
                                  context,
                                  IssueMapper.statusToString(issue.issueStatus),
                                  Icons.replay_circle_filled_rounded,
                                  Colors.teal,
                                  Colors.teal),
                              SizedBox(
                                width: 8,
                              ),
                              coloredBox(
                                  context,
                                  IssueMapper.categoryToString(
                                      issue.issueCategory),
                                  _getIcon(IssueMapper.categoryToString(
                                      issue.issueCategory)),
                                  _getTextOrBorderColor(
                                      IssueMapper.categoryToString(
                                          issue.issueCategory)),
                                  _getTextOrBorderColor(
                                      IssueMapper.categoryToString(
                                          issue.issueCategory))),
                              SizedBox(
                                width: 8,
                              ),
                              coloredBox(
                                  context,
                                  IssueMapper.priorityToString(
                                      issue.issuePriority),
                                  Icons.show_chart,
                                  _getPriorityTextColor(
                                      IssueMapper.priorityToString(
                                          issue.issuePriority)),
                                  _getBackgroundColor(
                                      IssueMapper.priorityToString(
                                          issue.issuePriority))),
                              SizedBox(
                                width: 8,
                              ),
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                ),
                flex: 8,
              ),
            ],
          ),
        ),
        elevation: 8,
        margin: EdgeInsets.all(10),
      ),
    );
  }

  Color _getBackgroundColor(String category) {
    switch (category) {
      case 'Low':
        return Colors.purple.withOpacity(0.3);
      case 'Medium':
        return Color(0xff0C7800).withOpacity(0.3);
      case 'Critical':
        return Color(0xff980000).withOpacity(0.3);
      case 'High':
        return Colors.orange.withOpacity(0.3);
      default:
        return Colors.black.withOpacity(0.3);
    }
  }

  Color _getTextOrBorderColor(String category) {
    switch (category) {
      case 'General':
        return Color(0xff3A35C4);
      case 'Images':
        return Color(0xff0C7800);
      case 'Labels':
        return Color(0xff980000);
      case 'Models':
        return Color(0xffCBBD00);
      case 'Labelling':
        return Color(0xfff26d5b);
      default:
        return Colors.black;
    }
  }

  IconData _getIcon(String role) {
    switch (role) {
      case 'Images':
        return Icons.image;
      case 'Labels':
        return Icons.label;
      case 'Labelling':
        return Icons.image_search_rounded;
      case 'Models':
        return Icons.model_training;
      default:
        return Icons.people;
    }
  }

  Color _getPriorityTextColor(String category) {
    switch (category) {
      case 'Low':
        return Colors.purple;
      case 'Medium':
        return Color(0xff0C7800);
      case 'Critical':
        return Color(0xff980000);
      case 'High':
        return Colors.orange;
      default:
        return Colors.black;
    }
  }

  Widget coloredBox(BuildContext context, String text, IconData icon,
      Color textColor, Color backgroundColor) {
    final size = MediaQuery.of(context).size;
    return Container(
        height: 30,
        width:  size.width * 0.27,
        decoration: BoxDecoration(
          color: isCustomized? backgroundColor.withOpacity(0.3) :Colors.teal.withOpacity(0.3),
          border: Border.all(
            width: 1,
            color: isCustomized?backgroundColor :Colors.teal,
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.only(left: 4),
          child: Row(
            children: [
              Icon(
                icon,
                size: 20,
                color:isCustomized? textColor:Colors.teal,
              ),
              SizedBox(
                width: 4,
              ),
              Text(
                text,
               
                style: TextStyle(color: isCustomized? textColor:Colors.teal),
              )
            ],
          ),
        ));
  }
}
