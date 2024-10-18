
# Architecture Decision Records (ADRs)

This document lists the important architecture decisions for the Software System.

## Decision 001: Use Relational Database

- **Status**: Accepted
- **Date**: 2024-01-01
- **Context**: The system needs to store user data, which is highly structured.
- **Decision**: Use a relational database (MySQL) for its robustness and ACID guarantees.
- **Consequences**: Ensures data consistency and is easy to manage.

## Decision 002: Use Java for Backend Development

- **Status**: Accepted
- **Date**: 2024-01-02
- **Context**: The development team is well-versed in Java, and the system needs a robust framework.
- **Decision**: Use Java with Spring Boot for backend development.
- **Consequences**: Enables rapid development while leveraging team expertise.
    