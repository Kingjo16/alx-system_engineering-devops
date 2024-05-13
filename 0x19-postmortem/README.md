**Issue Summary:**

- **Duration:** 12 hours, from 2024-05-12 14:00 UTC to 2024-05-13 02:00 UTC.
- **Impact:** The web application experienced intermittent downtime, affecting approximately 30% of users. Users reported slow loading times and intermittent errors.

**Root Cause:**

The root cause of the outage was identified as a database deadlock issue triggered by a recent deployment that introduced a poorly optimized database query.

**Timeline:**

- **2024-05-12 14:00 UTC:** The issue was detected by automated monitoring alerts indicating increased response times.
- **2024-05-12 14:10 UTC:** The engineering team was notified of the issue.
- **2024-05-12 14:15 UTC:** Initial investigation focused on frontend servers and network connectivity but found no abnormalities.
- **2024-05-12 14:30 UTC:** Database logs were examined, revealing a spike in deadlock errors coinciding with the onset of performance issues.
- **2024-05-12 15:00 UTC:** Development team identified a recently deployed query optimization as a potential cause.
- **2024-05-12 15:30 UTC:** Attempts to roll back the optimization were made, but the issue persisted.
- **2024-05-12 16:00 UTC:** Incident escalated to database administrators for further analysis.
- **2024-05-12 18:00 UTC:** Database administrators confirmed the deadlock issue and identified the specific query causing it.
- **2024-05-12 20:00 UTC:** Temporary workaround implemented to mitigate the impact on users.
- **2024-05-13 02:00 UTC:** Permanent fix deployed to address the root cause.

**Root Cause and Resolution:**

The root cause of the issue was a deadlock caused by a database query that was inefficiently optimized. The query was locking rows unnecessarily, leading to contention and eventual deadlocks under high load.

To resolve the issue, the development team optimized the offending query to minimize locking and reduce contention. Additionally, database indexes were adjusted to improve query performance and reduce the likelihood of deadlocks occurring in the future.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:**
  - Implement stricter code review processes for database query optimizations to catch potential performance issues earlier.
  - Enhance monitoring and alerting systems to provide more granular insights into database performance and deadlock occurrences.
  - Conduct regular performance audits to identify and address inefficiencies in database queries and indexing strategies.

- **Tasks to Address the Issue:**
  - Review and optimize all recently deployed database queries for efficiency and performance.
  - Conduct a comprehensive review of database indexes to ensure they are properly configured to support query optimization.
  - Enhance monitoring and alerting systems to provide real-time visibility into database performance and detect potential deadlock issues proactively.

By implementing these corrective and preventative measures, we aim to minimize the risk of similar incidents occurring in the future and ensure the continued reliability and performance of our web application.
