--
-- Table structure for table `users`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE IF NOT EXISTS users (
        id         INTEGER  NOT NULL AUTO_INCREMENT,
        first_name VARCHAR (20) NOT NULL,
        last_name  VARCHAR (20) NOT NULL,
        email      VARCHAR (150) NOT NULL,
        PASSWORD   VARCHAR (150) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `exercises`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE IF NOT EXISTS exercises
             (
                          id            INTEGER NOT NULL AUTO_INCREMENT,
                          exercise_name VARCHAR(50) NOT NULL,
                          sets          INTEGER NOT NULL,
                          reps          INTEGER NOT NULL,
                          muscle_group  VARCHAR(50) NOT NULL,
                          description   VARCHAR(10000) NOT NULL,
                          image         VARCHAR(100) NOT NULL,
                          user_id       INTEGER NOT NULL,
                          PRIMARY KEY (id),
                          FOREIGN KEY(user_id) REFERENCES users (id)
                )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
