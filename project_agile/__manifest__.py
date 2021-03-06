# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Project Agile",
    "summary": "This module provides core framework for development of all agile methodologies like kanban, scrum, etc",
    "category": "Project",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "author": "Modoolar",
    "website": "https://www.modoolar.com/",

    "depends": [
        "web",
        "project_key",
        "project_workflow",
        "hr_timesheet",
        "web_syncer",
        "website",
        "web_editor",
        "project_portal",
    ],

    "data": [
        # security
        "security/security.xml",
        "security/ir.model.access.csv",

        # wizards
        "wizards/board_export_wizard.xml",
        "wizards/board_import_wizard.xml",
        "wizards/board_create_wizard.xml",
        "wizards/project_task_worklog_wizard.xml",
        "wizards/add_subtask_wizard.xml",
        "wizards/add_task_link_wizard.xml",
        "wizards/stage_change_confirmation_wizard.xml",

        # views
        "views/project_project_views.xml",
        "views/project_task_views.xml",
        "views/project_workflow.xml",
        "views/project_agile_team_views.xml",
        "views/project_agile_board_views.xml",

        # TODO: Merger this files into one file called ``webclient_templates.xml``

        # Web assets
        "views/project_agile_web_assets.xml",

        "views/templates.xml",
        "views/agile_assets.xml",

        # Project Portal
        'views/project_portal_assets.xml',
        'views/project_portal_templates.xml',

        # Menus
        "views/menu.xml",

        # data
        "data/project_task.xml",
        "data/project_project.xml",
    ],

    "demo": [
    ],

    "qweb": ["static/src/xml/*.xml"],
    "post_init_hook": "post_init_hook",
    "application": False,
    "installable": True,
}