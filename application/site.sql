-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exercises`
--

DROP TABLE IF EXISTS `exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE exercises 
             ( 
                          id            INTEGER NOT NULL, 
                          exercise_name VARCHAR(50) NOT NULL, 
                          sets          INTEGER NOT NULL, 
                          reps          INTEGER NOT NULL, 
                          muscle_group  VARCHAR(50) NOT NULL, 
                          description   VARCHAR(100000) NOT NULL, 
                          image         VARCHAR(20) NOT NULL, 
                          user_id       INTEGER NOT NULL, 
                          PRIMARY KEY (id), 
                          FOREIGN KEY(user_id) REFERENCES users (id)
		)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises`
--

LOCK TABLES `exercises` WRITE;
/*!40000 ALTER TABLE `exercises` DISABLE KEYS */;
INSERT INTO `exercises` VALUES (1,'Squat',6,8,'Legs','Stand with your feet apart, directly under your hips, and place your hands on your hips. Standing up tall, put your shoulders back, lift your chest, and pull in your abdominal muscles. Bend your knees while keeping your upper body as straight as possible, as if you were lowering yourself onto a seat behind you. Lower yourself as far as you can without leaning your upper body more than a few inches forward.  Tip: Don’t allow your knees to go too far forward. You don’t want them to stick out past your toes. Being careful not to lock your knees when you reach a standing position, straighten your legs.','/static/picture_uploads/squat.png',1),(2,'Lateral Raises',4,12,'Shoulders','Stand or sit with a dumbbell in each hand at your sides. Keep your back straight, brace your core, and then slowly lift the weights out to the side until your arms are parallel with the floor, with the elbow slightly bent. Then lower them back down, again in measured fashion.','/static/picture_uploads/shoulderpress2.jpg',1),(3,'Dumbbell Shoulder Press',5,6,'Shoulders','Hold the dumbbells by your shoulders with your palms facing forwards and your elbows out to the sides and bent at a 90° angle. Without leaning back, extend through your elbows to press the weights above your head. Then slowly return to the starting position.','/static/picture_uploads/shoulderpress.jpg',1),(4,'Bench Press',5,5,'Chest','Lie on the bench with your eyes under the bar. Grab the bar with a medium grip-width (thumbs around the bar!). Unrack the bar by straightening your arms. Lower the bar to your mid-chest. Press the bar back up until your arms are straight.','/static/picture_uploads/bench.png',1),(5,'Dumbbell Chest Fly',4,10,'Chest','Lie with your head and shoulders supported by the bench and your feet flat on the floor. Hold the dumbbells directly above your chest, palms facing each other, then lower the weights in an arc out to the sides as far as is comfortable. Use your pectoral muscles to reverse the movement back to the start. Keep a slight bend in your elbows throughout and don’t arch your back.','/static/picture_uploads/flys.png',1),(6,'Dumbbell Lunge',6,10,'Legs','Stand up straight with a dumbbell in each hand. Hang your arms at ​your sides. Palms should face the thighs (hammer grip). Feet should be a little less than shoulder-width apart.​ Take a big step forward with either leg, bending at the knee until the front thigh approaches parallel to the ground, landing on the heel. Inhale as you go down. The rear leg is bent at the knee and balanced on the toes. For the leg you step forward with, don\'t let the knee go past the tip of the toes. Step back to your standing starting position while exhaling. Repeat the motion with the other leg. ','/static/picture_uploads/lunges.png',1),(7,'Deadlift',8,8,'Back','    With your feet flat beneath the barbell, squat down and grasp it with your hands roughly shoulder-width apart.     Keep your chest up, pull your shoulders back and look straight ahead rather than up or down.     Lift the bar, keeping it close to your legs and focus on taking the weight back onto your heels (rather than your toes). Think about pulling the weight towards you on the way up. Lift to thigh level, pause, then return under control to the start position.     Let the weight come to a complete rest between each rep. While it\'s on the floor, take a second or two to make sure your body is in the correct position – chest up, upper back tight and eyes looking forward – before lifting it up again. ','/static/picture_uploads/deadlift.png',1),(8,'Rack Pull',5,5,'Back','When the bar is in your favoured position, grasp it with your palms facing towards you and your hands shoulder-width apart. Engage your hamstrings by pushing your hips back. Keeping your back straight and looking forwards throughout the movement, lift the weight by driving your hips forwards and straightening your knees. Pull your shoulders back at the top of the movement, then slowly reverse the movement and lower the bar back into the power rack.','/static/picture_uploads/rack-pull.png',1),(9,'Tricep Pull-Down',4,15,'Arms','Start by bracing your abdominals. Tuck your elbows in at your sides and position your feet slightly apart. Inhale. Push down until your elbows are fully extended but not yet in the straight, locked position. Keep your elbows close to your body and bend your knees slightly on the pushdown. Resist bending forward. Try to keep your back as straight as possible as you push down. As you exhale, return to the starting point using a controlled movement.','/static/picture_uploads/tricep.png',1),(10,'Bicep Curl',4,15,'Arms','    Stand with feet hip distance apart. Start by holding the dumbbells down next to the sides of your legs with arms fully extended, a slight bend in the elbow and palms facing forward.     Bend your elbows and curl your dumbbells up to your shoulders, make sure you curl all the way to the top.     Lower the weights back down making sure to straighten your arms until they are next to your legs where you started.','/static/picture_uploads/bicep.png',1),(11,'Crunches',4,15,'Core','  Lie on your back with your knees bent and feet flat on the floor, hip-width apart.  Place your hands behind your head so your thumbs are behind your ears.  Don’t lace your fingers together.  Hold your elbows out to the sides but rounded slightly in.  Tilt your chin slightly, leaving a few inches of space between your chin and your chest.  Gently pull your abdominals inward.  Curl up and forward so that your head, neck, and shoulder blades lift off the floor.  Hold for a moment at the top of the movement and then lower slowly back down.','/static/picture_uploads/crunches.png',1),(12,'Hanging Leg Raise',3,8,'Core','    Hang from a bar using a shoulder-width pronated (overhand) grip.     Straighten your lower back so that there is as little of an arch in your lower back as possible. Keeping your body still, lower back straight and legs together, exhale as you slowly raise your knees by flexing your hips. Hold for a count of two. Inhale as you slowly lower your knees to the starting position by extending your hips.','/static/picture_uploads/hangingleg.png',1),(13,'High Cable Cross Over',4,12,'Chest','Grasp the stirrup of the left pulley with your left hand and the stirrup of the right pulley with your right hand using an overhand grip. Bend forward a little by flexing your hips and knees. Internally rotate your shoulders so that your elbows are shoulder height. Keeping your elbows slightly bent, exhale as you slowly pull the stirrups together in a downward hugging motion. Hold for a count of two and squeeze your chest. Inhale as you slowly reverse the motion until you feel a slight stretch in your chest.','/static/picture_uploads/crossover.png',1);
/*!40000 ALTER TABLE `exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE users ( 
        id         INTEGER  NOT NULL, 
        first_name VARCHAR (20) NOT NULL, 
        last_name  VARCHAR (20) NOT NULL, 
        email      VARCHAR (150) NOT NULL, 
        PASSWORD   VARCHAR (50) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Eoghan','Winters','eoghanwinters@qa.com','$2b$12$TmIPW6A/.Jwboj6DLUDUCug1l/WG5.XxpT9MsCNxPJXeamLjWNtxq');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:24
