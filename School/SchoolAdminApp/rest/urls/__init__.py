from django.urls import include, path


urlpatterns = [
    path(
        "libraries/",
        include("SchoolAdminApp.rest.urls.library"),
    ),
    
    path(
        "transports/",
        include("SchoolAdminApp.rest.urls.transport"),
    ),

    path(
        "hostels/",
        include("SchoolAdminApp.rest.urls.hostel"),
    ),

    path(
        "sports/",
        include("SchoolAdminApp.rest.urls.sports_information"),
    ),

    path(
        "class-time-tables/",
        include("SchoolAdminApp.rest.urls.class_time_table"),
    ),

    path(
        "department/",
        include("SchoolAdminApp.rest.urls.department"),
    ),

    path(
        "exams/",
        include("SchoolAdminApp.rest.urls.exam"),
    ),

    path(
        "subject/",
        include("SchoolAdminApp.rest.urls.subject"),

    ),
    
    path(
        "career/",
        include("SchoolAdminApp.rest.urls.career"),

    ),

    path(
        "candidate/",
        include("SchoolAdminApp.rest.urls.candidate"),

    ),

    path(
        "vendor/",
        include("SchoolAdminApp.rest.urls.vendor"),

    ),

    path(
        "product/category/",
        include("SchoolAdminApp.rest.urls.category"),

    ),

    path(
        "product/",
        include("SchoolAdminApp.rest.urls.product"),

    ),

    path(
        "product/purchase/request/",
        include("SchoolAdminApp.rest.urls.purchasesRequest"),
    ),
    
    path(
        "product/purchase/received/",
        include("SchoolAdminApp.rest.urls.purchaseReceived"),
    ),

    path(
        "holiday/",
        include("SchoolAdminApp.rest.urls.holiday"),
    ),

    path(
        "fees/category/",
        include("SchoolAdminApp.rest.urls.feesCategory"),
    ),
    
    path(
        "fees/information/",
        include("SchoolAdminApp.rest.urls.feesInformation"),
    ),

    path(
        "fees/collection/",
        include("SchoolAdminApp.rest.urls.feesCollection"),
    ),
    path(
        "grading-config/",
        include("SchoolAdminApp.rest.urls.grading_config"),
    ),
    path(
        "semester/",
        include("SchoolAdminApp.rest.urls.semester")
    )
]
