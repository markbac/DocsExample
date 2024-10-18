
workspace {

    model {
        user = person "User" "A user of the system"
        softwareSystem = softwareSystem "Software System" {
            webapp = container "Web Application" "Delivers content to users" "Java and Spring Boot"
            database = container "Database" "Stores user data" "MySQL"

            user -> webapp "Uses"
            webapp -> database "Reads from and writes to"
        }
    }

    views {
        systemContext softwareSystem {
            include *
            autolayout lr
        }

        container softwareSystem {
            include *
            autolayout lr
        }

        theme default
    }

    styles {
        element "Database" {
            background #facc2e
        }
    }

    documentation {
        softwareSystem {
            adr {
                decision "001" "Use relational database" {
                    status "Accepted"
                    date "2024-01-01"
                    context "The system needs to store user data, which is highly structured."
                    decision "Use a relational database (MySQL) for its robustness and ACID guarantees."
                    consequences "Ensures data consistency and is easy to manage."
                }
                decision "002" "Use Java for backend development" {
                    status "Accepted"
                    date "2024-01-02"
                    context "The development team is well-versed in Java, and the system needs a robust framework."
                    decision "Use Java with Spring Boot for backend development."
                    consequences "Enables rapid development while leveraging team expertise."
                }
            }
        }
    }
}
