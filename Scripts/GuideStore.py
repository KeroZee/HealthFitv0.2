from flask import flash

from Scripts.Exercises import Exercises
import shelve

storing = shelve.open('store_ex')

if storing['exer0'] == None:
    # flash(f"{storing['exer0']}", 'success')
    exercises_list = []
    e1 = Exercises(
        "A Push-up is a common exercise that involves beginning from the prone position,then raising and lowering the body using the arms.",
        ['Pectoral muscles',
         'Abdominal muscles',
         'Triceps'],
        ["Extend your legs backwards and place hands on the ground, slightly more than shoulder-width apart.",
         "Start by bending your elbows to lower your chest until it is just above the floor.",
         "Push yourself back to the starting position. An ideal push-up would be a 1-second push, pause and a 2 second down count.",
         "Repeat steps 1 to 3 for preferably 10 to 15 times."],
        "https://cdn-ami-drupal.heartyhosting.com/sites/muscleandfitness.com/files/styles/full_node_image_1090x614/public/media/1109-pushups_0.jpg?itok=QyFVWqN6",
        "https://www.youtube.com/embed/IODxDxX7oi4")
    e2 = Exercises(
        'Crunching is an exercise that involves lying face-up on the floor, bending the knees then curling the shoulders towards the waist.',
        ['Abdominal muscles'],
        ['Lie on your back with your knees bent and feet flat on the floor hip-width apart.',
         'Place your hands behind your head such that your thumbs are behind your ears',
         'Hold your elbows to the sides, slightly facing in.',
         'Slightly tilt your chin, leaving some space between your chin and chest.',
         'Gently pull your abdominals inward.',
         'Curl up and forward so that your head, neck and shoulders lift off the floor',
         'Hold for a moment at the top of the movement in Step 6 and slowly lower yourself back down',
         'Repeat Steps 1 to 7 for preferably 10 to 15 times.'],
        "https://cdn2.coachmag.co.uk/sites/coachmag/files/styles/16x9_480/public/images/dir_30/mens_fitness_15427.jpg?itok=T3OF7wPv&timestamp=1369282187",
        "https://www.youtube.com/embed/Xyd_fa5zoEU")
    e3 = Exercises(
        'Jumping Jacks is an exercise that involves jumping with the legs spread wide and hands touching overhead then returning to a position with the feet together and arms at the sides.',
        ['Calve muscles',
         'Shoulder muscles',
         'Hip muscles'],
        ['Stand with your feet together and pointing forward, arms hanging straight at the sides.',
         'In one jump, bend your knees and extend both legs out to the sides while simultaneously extending your arms out to the sides and then up and over the head.',
         'Immediately reverse this motion, jumping back to the starting or neutral standing position.',
         'Repeat Steps 1 to 3 for preferably 10 to 15 times.'],
        "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/1104-jumping-jacks-1441032989.jpg",
        "https://www.youtube.com/embed/UpH7rm0cYbM")
    e4 = Exercises(
        'Tuck jumping is an exercise that involves standing in a shoulder width position, slowly descending into a squat and use your feet to explode off the floor while driving your knees towards your chest.',
        ['Abdominal muscles',
         'Hamstrings',
         'Calve muscles'],
        ['Start in a standing position, slightly bending your knees',
         'Hold your hands out at chest level.',
         'Lower your body quickly into a squatting position, then explode upwards bringing your knees up towards your chest.',
         'Repeat Steps 1 to 3 for preferably 10 to 15 times.'],
        "http://fitmw.com/wp-content/uploads/2015/07/Exercises-Tuck-Jump.jpg",
        "https://www.youtube.com/embed/ZR6aFqdRi2Y")
    e5 = Exercises(
        'Squatting is an exercise that involves standing in a shoulder width position, bending your knees all the way down and then suddenly propelling yourself back up to a standing position.',
        ['Hip muscles',
         'Hamstrings',
         'Quads'],
        ['Stand with your feet apart, directly under your hips, and place your hands on your hips.',
         'Standing up tall, put your shoulders back, lift your chest, and pull in your abdominal muscles.',
         'Bend your knees while keeping your upper body as straight as possible, like a sitting position. Lower yourself down as far as you can without leaning your upper body more than a few inches forward.',
         'Straighten your legs so you do not lock your knees when you reach a standing position.',
         'Repeat Steps 1 to 4 for preferably 10 to 15 times.'],
        "https://19jkon2dxx3g14btyo2ec2u9-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/squats.jpg",
        "https://www.youtube.com/embed/aclHkVaku9U")
    e6 = Exercises(
        'Flutter kicks is an exercise that involves lying down face-up, straightening your legs until they are level with your hips and alternating between lifting each leg.',
        ['Abdominal muscles',
         'Hip muscles',
         'Quads'],
        ['Lie on your back with your legs extended and your arms alongside your hips, palms down.',
         'Lift your legs about 4 to 6 inches off the floor. Press your lower back into the floor or gym mat.',
         'Keep your legs straight as you rhythmically raise one leg higher, then switch. Move in a fluttering, up and down motion.',
         'Repeat Steps 1 to 3 for preferably 15 to 20 times.'],
        "https://i.pinimg.com/originals/74/d8/55/74d855acc30ffdfe3c7410f3c278918b.jpg",
        "https://www.youtube.com/embed/ANVdMDaYRts")
    exercises_list.extend([e1, e2, e3, e4, e5, e6])
    for i in range(5):
        storing['exer' + str(i)] = exercises_list[i]
    storing.close()
