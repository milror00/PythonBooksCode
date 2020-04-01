

def selection_sort(unsorted_list):

    size_of_list = len(unsorted_list)

    for i in range(size_of_list):
        for j in range(i+1, size_of_list):

            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp


a_list = [3, 2, 35, 4, 32, 94, 5, 7]
selection_sort(a_list)
print(a_list)


my_1 = sorted([ 2622, 1179, 4687, 652, 72, 676, 988, 999, 264, 580, 380, 843, 30, 273, 949, 108, 147, 684, 12, 947, 719, 786, 770, 970, 479, 577, 260, 722, 101, 802, 117, 751, 159, 683, 478, 699, 23, 730, 1, 69, 16, 359, 820, 111, 195, 867, 293, 774, 646, 456, 537, 696, 8, 331, 2, 378, 783, 15, 310, 489, 725, 752, 872, 519, 709, 704, 502, 554, 525, 43, 49, 201, 437, 850, 369, 840, 157, 362, 738, 847, 959, 263, 254, 511, 445, 21, 992, 995, 221, 410, 953, 567, 47, 904, 654, 4, 145, 154, 584, 726, 809, 113, 510, 906, 458, 529, 923, 405, 241, 334, 771, 924, 176, 763, 104, 79, 897, 905, 931, 972, 210, 357, 805, 532, 522, 920, 152, 446, 619, 780, 205, 372, 748, 197, 84, 128, 919, 824, 505, 513, 628, 883, 749, 720, 610, 591, 740, 921, 816, 729, 194, 769, 429, 979, 9, 137, 549, 361, 721, 621, 945, 509, 358, 347, 233, 388, 552, 935, 37, 272, 124, 943, 56, 839, 822, 526, 606, 804, 421, 285, 455, 431, 553, 530, 160, 255, 346, 370, 671, 501, 568, 870, 670, 301, 26, 957, 838, 605, 337, 77, 173, 878, 395, 815, 996, 95, 184, 102, 28, 403, 785, 3, 852, 521, 106, 332, 149, 508, 663, 232, 733, 408, 627, 773, 439, 485, 607, 868, 189, 691, 167, 266, 793, 200, 284, 634, 344, 404, 374, 170, 419, 967, 582, 542, 776, 861, 432, 180, 678, 63, 611, 948, 146, 242, 73, 468, 276, 639, 910, 724, 702, 35, 14, 138, 300, 735, 119, 563, 856, 70, 292, 87, 966, 319, 764, 833, 902, 928, 345, 570, 708, 916, 227, 46, 877, 637, 385, 622, 968, 57, 96, 960, 812, 941, 603, 766, 33, 514, 488, 848, 389, 188, 391, 140, 718, 80, 781, 544, 656, 474, 473, 226, 693, 692, 10, 231, 792, 120, 107, 237, 235, 857, 100, 126, 638, 727, 686, 430, 750, 186, 596, 327, 428, 433, 575, 314, 60, 993, 31, 775, 394, 969, 716, 990, 491, 889, 682, 885, 330, 282, 800, 539, 915, 650, 977, 760, 336, 277, 616, 667, 743, 443, 228, 958, 899, 806, 562, 382, 875, 174, 499, 175, 620, 134, 506, 191, 756, 528, 299, 865, 462, 784, 703, 817, 434, 705, 262, 493, 971, 425, 18, 823, 504, 397, 578, 130, 645, 326, 366, 298, 655, 144, 68, 609, 288, 465, 187, 520, 534, 666, 886, 351, 565, 424, 169, 909, 92, 779, 495, 469, 798, 339, 761, 295, 246, 507, 305, 535, 414, 976, 459, 182, 317, 41, 38, 34, 55, 894, 141, 387, 778, 352, 887, 271, 444, 713, 965, 267, 460, 5, 11, 669, 772, 932, 323, 481, 825, 643, 675, 517, 895, 484, 311, 866, 685, 701, 422, 922, 129, 767, 291, 151, 234, 166, 40, 841, 348, 442, 436, 835, 561, 879, 617, 463, 315, 647, 85, 118, 980, 858, 384, 498, 631, 377, 373, 747, 753, 392, 845, 304, 665, 6, 613, 707, 278, 937, 229, 827, 739, 624, 181, 731, 401, 629, 492, 794, 360, 907, 383, 390, 127, 91, 754, 269, 854, 407, 579, 997, 179, 363, 222, 29, 818, 67, 381, 533, 864, 759, 165, 325, 541, 447, 985, 768, 664, 572, 569, 62, 376, 546, 649, 153, 343, 732, 253, 239, 788, 888, 808, 148, 417, 155, 681, 900, 810, 908, 486, 626, 615, 453, 349, 882, 303, 602, 22, 464, 121, 516, 597, 527, 821, 353, 251, 420, 844, 623, 338, 547, 413, 290, 243, 448, 855, 714, 208, 698, 17, 836, 472, 813, 862, 653, 131, 706, 586, 426, 545, 765, 368, 163, 636, 364, 112, 891, 329, 39, 98, 250, 178, 86, 99, 480, 612, 316, 559, 550, 677, 688, 830, 198, 225, 737, 642, 321, 257, 983, 956, 736, 335, 259, 294, 238, 74, 164, 608, 103, 599, 846, 449, 660, 961, 258, 811, 409, 876, 135, 90, 487, 697, 450, 633, 476, 694, 427, 415, 306, 543, 914, 375, 651, 162, 787, 672, 695, 302, 58, 863, 942, 566, 202, 557, 929, 849, 354, 998, 441, 828, 477, 25, 604, 418, 475, 829, 328, 640, 289, 819, 123, 114, 402, 588, 901, 954, 215, 82, 411, 65, 658, 496, 83, 283, 576, 930, 247, 680, 745, 583, 564, 185, 193, 981, 789, 470, 585, 757, 851, 890, 268, 859, 158, 320, 795, 340, 161, 762, 801, 592, 635, 142, 497, 917, 589, 940, 212, 280, 964, 618, 978, 171, 986, 755, 230, 371, 538, 196, 911, 240, 211, 287, 110, 416, 950, 379, 926, 741, 312, 396, 832, 710, 313, 435, 7, 367, 982, 842, 952, 531, 333, 452, 71, 662, 700, 494, 356, 962, 782, 884, 512, 536, 690, 318, 573, 927, 641, 975, 342, 936, 540, 711, 236, 657, 89, 308, 109, 61, 717, 81, 355, 893, 24, 912, 133, 177, 524, 1000, 797, 168, 963, 76, 423, 734, 50, 365, 632, 143, 551, 406, 466, 939, 27, 256, 803, 548, 54, 898, 601, 261, 341, 207, 350, 451, 723, 386, 853, 249, 881, 918, 42, 286, 871, 500, 791, 461, 190, 814, 471, 644, 206, 807, 48, 973, 274, 393, 974, 51, 873, 204, 796, 296, 248, 88, 214, 594, 659, 744, 324, 587, 399, 44, 398, 203, 860, 987, 777, 571, 595, 223, 218, 115, 903, 689, 555, 172, 503, 673, 991, 139, 758, 614, 955, 97, 78, 728, 219, 270, 593, 648, 245, 440, 944, 483, 192, 116, 674, 309, 156, 220, 281, 244, 122, 490, 799, 574, 590, 105, 581, 52, 400, 19, 457, 598, 45, 790, 946, 913, 679, 32, 984, 837, 869, 938, 252, 307, 600, 558, 625, 438, 925, 892, 136, 183, 59, 322, 661, 209, 826, 834, 934, 712, 217, 715, 454, 213, 951, 64, 746, 75, 482, 66, 994, 874, 150, 933, 297, 467, 216, 13, 36, 125, 523, 224, 275, 20, 93, 880, 989, 630, 742, 412, 515, 560, 831, 556, 53, 668, 518, 896, 132, 199, 94 ])
my_array = [ 2622, 1179, 4687, 652, 72, 676, 988, 999, 264, 580, 380, 843, 30, 273, 949, 108, 147, 684, 12, 947, 719, 786, 770, 970, 479, 577, 260, 722, 101, 802, 117, 751, 159, 683, 478, 699, 23, 730, 1, 69, 16, 359, 820, 111, 195, 867, 293, 774, 646, 456, 537, 696, 8, 331, 2, 378, 783, 15, 310, 489, 725, 752, 872, 519, 709, 704, 502, 554, 525, 43, 49, 201, 437, 850, 369, 840, 157, 362, 738, 847, 959, 263, 254, 511, 445, 21, 992, 995, 221, 410, 953, 567, 47, 904, 654, 4, 145, 154, 584, 726, 809, 113, 510, 906, 458, 529, 923, 405, 241, 334, 771, 924, 176, 763, 104, 79, 897, 905, 931, 972, 210, 357, 805, 532, 522, 920, 152, 446, 619, 780, 205, 372, 748, 197, 84, 128, 919, 824, 505, 513, 628, 883, 749, 720, 610, 591, 740, 921, 816, 729, 194, 769, 429, 979, 9, 137, 549, 361, 721, 621, 945, 509, 358, 347, 233, 388, 552, 935, 37, 272, 124, 943, 56, 839, 822, 526, 606, 804, 421, 285, 455, 431, 553, 530, 160, 255, 346, 370, 671, 501, 568, 870, 670, 301, 26, 957, 838, 605, 337, 77, 173, 878, 395, 815, 996, 95, 184, 102, 28, 403, 785, 3, 852, 521, 106, 332, 149, 508, 663, 232, 733, 408, 627, 773, 439, 485, 607, 868, 189, 691, 167, 266, 793, 200, 284, 634, 344, 404, 374, 170, 419, 967, 582, 542, 776, 861, 432, 180, 678, 63, 611, 948, 146, 242, 73, 468, 276, 639, 910, 724, 702, 35, 14, 138, 300, 735, 119, 563, 856, 70, 292, 87, 966, 319, 764, 833, 902, 928, 345, 570, 708, 916, 227, 46, 877, 637, 385, 622, 968, 57, 96, 960, 812, 941, 603, 766, 33, 514, 488, 848, 389, 188, 391, 140, 718, 80, 781, 544, 656, 474, 473, 226, 693, 692, 10, 231, 792, 120, 107, 237, 235, 857, 100, 126, 638, 727, 686, 430, 750, 186, 596, 327, 428, 433, 575, 314, 60, 993, 31, 775, 394, 969, 716, 990, 491, 889, 682, 885, 330, 282, 800, 539, 915, 650, 977, 760, 336, 277, 616, 667, 743, 443, 228, 958, 899, 806, 562, 382, 875, 174, 499, 175, 620, 134, 506, 191, 756, 528, 299, 865, 462, 784, 703, 817, 434, 705, 262, 493, 971, 425, 18, 823, 504, 397, 578, 130, 645, 326, 366, 298, 655, 144, 68, 609, 288, 465, 187, 520, 534, 666, 886, 351, 565, 424, 169, 909, 92, 779, 495, 469, 798, 339, 761, 295, 246, 507, 305, 535, 414, 976, 459, 182, 317, 41, 38, 34, 55, 894, 141, 387, 778, 352, 887, 271, 444, 713, 965, 267, 460, 5, 11, 669, 772, 932, 323, 481, 825, 643, 675, 517, 895, 484, 311, 866, 685, 701, 422, 922, 129, 767, 291, 151, 234, 166, 40, 841, 348, 442, 436, 835, 561, 879, 617, 463, 315, 647, 85, 118, 980, 858, 384, 498, 631, 377, 373, 747, 753, 392, 845, 304, 665, 6, 613, 707, 278, 937, 229, 827, 739, 624, 181, 731, 401, 629, 492, 794, 360, 907, 383, 390, 127, 91, 754, 269, 854, 407, 579, 997, 179, 363, 222, 29, 818, 67, 381, 533, 864, 759, 165, 325, 541, 447, 985, 768, 664, 572, 569, 62, 376, 546, 649, 153, 343, 732, 253, 239, 788, 888, 808, 148, 417, 155, 681, 900, 810, 908, 486, 626, 615, 453, 349, 882, 303, 602, 22, 464, 121, 516, 597, 527, 821, 353, 251, 420, 844, 623, 338, 547, 413, 290, 243, 448, 855, 714, 208, 698, 17, 836, 472, 813, 862, 653, 131, 706, 586, 426, 545, 765, 368, 163, 636, 364, 112, 891, 329, 39, 98, 250, 178, 86, 99, 480, 612, 316, 559, 550, 677, 688, 830, 198, 225, 737, 642, 321, 257, 983, 956, 736, 335, 259, 294, 238, 74, 164, 608, 103, 599, 846, 449, 660, 961, 258, 811, 409, 876, 135, 90, 487, 697, 450, 633, 476, 694, 427, 415, 306, 543, 914, 375, 651, 162, 787, 672, 695, 302, 58, 863, 942, 566, 202, 557, 929, 849, 354, 998, 441, 828, 477, 25, 604, 418, 475, 829, 328, 640, 289, 819, 123, 114, 402, 588, 901, 954, 215, 82, 411, 65, 658, 496, 83, 283, 576, 930, 247, 680, 745, 583, 564, 185, 193, 981, 789, 470, 585, 757, 851, 890, 268, 859, 158, 320, 795, 340, 161, 762, 801, 592, 635, 142, 497, 917, 589, 940, 212, 280, 964, 618, 978, 171, 986, 755, 230, 371, 538, 196, 911, 240, 211, 287, 110, 416, 950, 379, 926, 741, 312, 396, 832, 710, 313, 435, 7, 367, 982, 842, 952, 531, 333, 452, 71, 662, 700, 494, 356, 962, 782, 884, 512, 536, 690, 318, 573, 927, 641, 975, 342, 936, 540, 711, 236, 657, 89, 308, 109, 61, 717, 81, 355, 893, 24, 912, 133, 177, 524, 1000, 797, 168, 963, 76, 423, 734, 50, 365, 632, 143, 551, 406, 466, 939, 27, 256, 803, 548, 54, 898, 601, 261, 341, 207, 350, 451, 723, 386, 853, 249, 881, 918, 42, 286, 871, 500, 791, 461, 190, 814, 471, 644, 206, 807, 48, 973, 274, 393, 974, 51, 873, 204, 796, 296, 248, 88, 214, 594, 659, 744, 324, 587, 399, 44, 398, 203, 860, 987, 777, 571, 595, 223, 218, 115, 903, 689, 555, 172, 503, 673, 991, 139, 758, 614, 955, 97, 78, 728, 219, 270, 593, 648, 245, 440, 944, 483, 192, 116, 674, 309, 156, 220, 281, 244, 122, 490, 799, 574, 590, 105, 581, 52, 400, 19, 457, 598, 45, 790, 946, 913, 679, 32, 984, 837, 869, 938, 252, 307, 600, 558, 625, 438, 925, 892, 136, 183, 59, 322, 661, 209, 826, 834, 934, 712, 217, 715, 454, 213, 951, 64, 746, 75, 482, 66, 994, 874, 150, 933, 297, 467, 216, 13, 36, 125, 523, 224, 275, 20, 93, 880, 989, 630, 742, 412, 515, 560, 831, 556, 53, 668, 518, 896, 132, 199, 94 ]
selection_sort(my_array)
print(my_array == my_1)