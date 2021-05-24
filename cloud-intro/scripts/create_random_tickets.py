import json
import sys
from datetime import datetime, timedelta

import numpy as np


def _get_one_record():
    locations = [
        "Location 143",
        "Location 165",
        "Location 204",
        "Location 93",
        "Location 108",
        "Location 161",
        "Location 46",
        "Location 42",
        "Location 229",
        "Location 98",
        "Location 69",
        "Location 172",
        "Location 51",
        "Location 44",
        "Location 142",
        "Location 36",
        "Location 135",
        "Location 15",
        "Location 79",
        "Location 55",
        "Location 179",
        "Location 171",
        "Location 56",
        "Location 224",
        "Location 131",
        "Location 54",
        "Location 136",
        "Location 2",
        "Location 40",
        "Location 70",
        "Location 115",
        "Location 197",
        "Location 59",
        "Location 212",
        "Location 245",
        "Location 141",
        "Location 232",
        "Location 18",
        "Location 125",
        "Location 241",
        "Location 128",
        "Location 96",
        "Location 249",
        "Location 91",
        "Location 170",
        "Location 208",
        "Location 162",
        "Location 9",
        "Location 153",
        "Location 117",
        "Location 218",
        "Location 111",
        "Location 100",
        "Location 71",
        "Location 33",
        "Location 39",
        "Location 112",
        "Location 72",
        "Location 97",
        "Location 68",
        "Location 193",
        "Location 210",
        "Location 113",
        "Location 158",
        "Location 124",
        "Location 37",
        "Location 196",
        "Location 85",
        "Location 47",
        "Location 24",
        "Location 43",
        "Location 14",
        "Location 77",
        "Location 109",
        "Location 41",
        "Location 38",
        "Location 226",
        "Location 240",
        "Location 76",
        "Location 99",
        "Location 213",
        "Location 118",
        "Location 82",
        "Location 35",
        "Location 199",
        "Location 28",
        "Location 242",
        "Location 78",
        "Location 107",
        "Location 45",
        "Location 247",
        "Location 3",
        "Location 216",
        "Location 133",
        "Location 86",
        "Location 12",
        "Location 231",
        "Location 223",
        "Location 10",
        "Location 177",
        "Location 83",
        "Location 187",
        "Location 160",
        "Location 220",
        "Location 209",
        "Location 5",
        "Location 190",
        "Location 173",
        "Location 205",
        "Location 34",
        "Location 64",
        "Location 25",
        "Location 110",
        "Location 114",
        "Location 235",
        "Location 134",
        "Location 207",
        "Location 225",
        "Location 221",
        "Location 237",
        "Location 234",
        "Location 194",
        "Location 168",
        "Location 17",
        "Location 211",
        "Location 90",
        "Location 138",
        "Location 92",
        "Location 81",
        "Location 195",
        "Location 222",
        "Location 60",
        "Location 182",
        "Location 8",
        "Location 27",
        "Location 169",
        "Location 101",
        "Location 75",
        "Location 228",
        "Location 236",
        "Location 21",
        "Location 174",
        "Location 66",
        "Location 6",
        "Location 233",
        "Location 203",
        "Location 201",
        "Location 214",
        "Location 140",
        "Location 157",
        "Location 243",
        "Location 155",
        "Location 102",
        "Location 13",
        "Location 120",
        "Location 244",
        "Location 188",
        "Location 11",
        "Location 185",
        "Location 65",
        "Location 23",
        "Location 49",
        "Location 186",
        "Location 248",
        "Location 87",
        "Location 61",
        "Location 129",
        "Location 148",
        "Location 184",
        "Location 183",
        "Location 149",
        "Location 137",
        "Location 95",
        "Location 167",
        "Location 200",
        "Location 30",
        "Location 147",
        "Location 166",
        "Location 20",
        "Location 122",
        "Location 130",
        "Location 227",
        "Location 146",
        "Location 156",
        "Location 176",
        "Location 206",
        "Location 175",
        "Location 52",
        "Location 215",
        "Location 189",
        "Location 144",
        "Location 180",
        "Location 219",
        "Location 22",
        "Location 31",
        "Location 121",
        "Location 73",
        "Location 53",
        "Location 239",
        "Location 29",
        "Location 89",
        "Location 164",
        "Location 26",
        "Location 178",
        "Location 63",
        "Location 119",
        "Location 151",
        "Location 123",
        "Location 145",
        "Location 191",
        "Location 57",
        "Location 16",
        "Location 181",
        "Location 132",
        "Location 116",
        "Location 94",
        "Location 217",
        "Location 19",
        "Location 105",
        "Location 50",
        "Location 4",
        "Location 106",
        "Location 202",
        "Location 246",
    ]
    categories = [
        "Category 55",
        "Category 40",
        "Category 20",
        "Category 9",
        "Category 53",
        "Category 44",
        "Category 45",
        "Category 42",
        "Category 32",
        "Category 8",
        "Category 24",
        "Category 61",
        "Category 37",
        "Category 26",
        "Category 23",
        "Category 62",
        "Category 17",
        "Category 13",
        "Category 35",
        "Category 43",
        "Category 34",
        "Category 19",
        "Category 46",
        "Category 63",
        "Category 51",
        "Category 22",
        "Category 30",
        "Category 31",
        "Category 15",
        "Category 47",
        "Category 7",
        "Category 57",
        "Category 25",
        "Category 56",
        "Category 38",
        "Category 49",
        "Category 4",
        "Category 28",
        "Category 41",
        "Category 36",
        "Category 54",
        "Category 29",
        "Category 3",
        "Category 27",
        "Category 33",
        "Category 58",
        "Category 2",
        "Category 21",
        "Category 16",
        "Category 50",
        "Category 59",
        "Category 12",
        "Category 52",
        "Category 5",
        "Category 6",
        "Category 10",
        "Category 48",
        "Category 14",
    ]
    subcategories = [
        "Subcategory 170",
        "Subcategory 215",
        "Subcategory 125",
        "Subcategory 97",
        "Subcategory 168",
        "Subcategory 229",
        "Subcategory 94",
        "Subcategory 185",
        "Subcategory 110",
        "Subcategory 164",
        "Subcategory 271",
        "Subcategory 220",
        "Subcategory 224",
        "Subcategory 9",
        "Subcategory 291",
        "Subcategory 194",
        "Subcategory 106",
        "Subcategory 191",
        "Subcategory 135",
        "Subcategory 175",
        "Subcategory 223",
        "Subcategory 130",
        "Subcategory 23",
        "Subcategory 47",
        "Subcategory 107",
        "Subcategory 127",
        "Subcategory 54",
        "Subcategory 75",
        "Subcategory 192",
        "Subcategory 303",
        "Subcategory 114",
        "Subcategory 120",
        "Subcategory 103",
        "Subcategory 200",
        "Subcategory 3",
        "Subcategory 123",
        "Subcategory 16",
        "Subcategory 270",
        "Subcategory 167",
        "Subcategory 144",
        "Subcategory 90",
        "Subcategory 31",
        "Subcategory 29",
        "Subcategory 13",
        "Subcategory 302",
        "Subcategory 113",
        "Subcategory 28",
        "Subcategory 109",
        "Subcategory 88",
        "Subcategory 117",
        "Subcategory 156",
        "Subcategory 150",
        "Subcategory 44",
        "Subcategory 162",
        "Subcategory 289",
        "Subcategory 80",
        "Subcategory 231",
        "Subcategory 83",
        "Subcategory 25",
        "Subcategory 153",
        "Subcategory 105",
        "Subcategory 277",
        "Subcategory 4",
        "Subcategory 189",
        "Subcategory 112",
        "Subcategory 78",
        "Subcategory 283",
        "Subcategory 154",
        "Subcategory 132",
        "Subcategory 225",
        "Subcategory 52",
        "Subcategory 208",
        "Subcategory 151",
        "Subcategory 176",
        "Subcategory 12",
        "Subcategory 301",
        "Subcategory 202",
        "Subcategory 65",
        "Subcategory 245",
        "Subcategory 173",
        "Subcategory 228",
        "Subcategory 40",
        "Subcategory 259",
        "Subcategory 275",
        "Subcategory 169",
        "Subcategory 86",
        "Subcategory 269",
        "Subcategory 251",
        "Subcategory 140",
        "Subcategory 6",
        "Subcategory 182",
        "Subcategory 20",
        "Subcategory 274",
        "Subcategory 207",
        "Subcategory 46",
        "Subcategory 57",
        "Subcategory 101",
        "Subcategory 261",
        "Subcategory 219",
        "Subcategory 50",
        "Subcategory 258",
        "Subcategory 174",
        "Subcategory 30",
        "Subcategory 305",
        "Subcategory 115",
        "Subcategory 166",
        "Subcategory 184",
        "Subcategory 67",
        "Subcategory 48",
        "Subcategory 294",
        "Subcategory 59",
        "Subcategory 89",
        "Subcategory 204",
        "Subcategory 227",
        "Subcategory 198",
        "Subcategory 262",
        "Subcategory 255",
        "Subcategory 116",
        "Subcategory 276",
        "Subcategory 177",
        "Subcategory 197",
        "Subcategory 99",
        "Subcategory 178",
        "Subcategory 11",
        "Subcategory 145",
        "Subcategory 69",
        "Subcategory 199",
        "Subcategory 292",
        "Subcategory 43",
        "Subcategory 8",
        "Subcategory 157",
        "Subcategory 282",
        "Subcategory 281",
        "Subcategory 179",
        "Subcategory 32",
        "Subcategory 298",
        "Subcategory 146",
        "Subcategory 161",
        "Subcategory 196",
        "Subcategory 260",
        "Subcategory 36",
        "Subcategory 124",
        "Subcategory 149",
        "Subcategory 92",
        "Subcategory 111",
        "Subcategory 118",
        "Subcategory 203",
        "Subcategory 100",
        "Subcategory 18",
        "Subcategory 159",
        "Subcategory 102",
        "Subcategory 17",
        "Subcategory 249",
        "Subcategory 296",
        "Subcategory 300",
        "Subcategory 142",
        "Subcategory 183",
        "Subcategory 250",
        "Subcategory 66",
        "Subcategory 248",
        "Subcategory 82",
        "Subcategory 233",
        "Subcategory 252",
        "Subcategory 68",
        "Subcategory 181",
        "Subcategory 218",
        "Subcategory 188",
        "Subcategory 60",
        "Subcategory 134",
        "Subcategory 243",
        "Subcategory 187",
        "Subcategory 226",
        "Subcategory 205",
        "Subcategory 247",
        "Subcategory 163",
        "Subcategory 64",
        "Subcategory 285",
        "Subcategory 217",
        "Subcategory 242",
        "Subcategory 138",
        "Subcategory 85",
        "Subcategory 172",
        "Subcategory 53",
        "Subcategory 10",
        "Subcategory 246",
        "Subcategory 72",
        "Subcategory 257",
        "Subcategory 171",
        "Subcategory 158",
        "Subcategory 235",
        "Subcategory 129",
        "Subcategory 77",
        "Subcategory 254",
        "Subcategory 56",
        "Subcategory 244",
        "Subcategory 232",
        "Subcategory 122",
        "Subcategory 240",
        "Subcategory 209",
        "Subcategory 42",
        "Subcategory 256",
        "Subcategory 74",
        "Subcategory 287",
        "Subcategory 84",
        "Subcategory 299",
        "Subcategory 279",
        "Subcategory 241",
        "Subcategory 236",
        "Subcategory 2",
        "Subcategory 213",
        "Subcategory 273",
        "Subcategory 141",
        "Subcategory 62",
        "Subcategory 160",
        "Subcategory 216",
        "Subcategory 195",
        "Subcategory 35",
        "Subcategory 212",
        "Subcategory 33",
        "Subcategory 34",
        "Subcategory 96",
        "Subcategory 211",
        "Subcategory 288",
        "Subcategory 280",
        "Subcategory 230",
        "Subcategory 45",
        "Subcategory 136",
        "Subcategory 104",
        "Subcategory 51",
        "Subcategory 210",
        "Subcategory 165",
        "Subcategory 253",
        "Subcategory 128",
        "Subcategory 234",
        "Subcategory 284",
        "Subcategory 193",
        "Subcategory 186",
        "Subcategory 264",
        "Subcategory 87",
        "Subcategory 222",
        "Subcategory 95",
        "Subcategory 119",
        "Subcategory 237",
        "Subcategory 304",
        "Subcategory 126",
        "Subcategory 37",
        "Subcategory 295",
        "Subcategory 152",
        "Subcategory 155",
        "Subcategory 131",
        "Subcategory 14",
        "Subcategory 71",
        "Subcategory 24",
        "Subcategory 22",
    ]
    symptoms = [
        "Symptom 72",
        "Symptom 471",
        "Symptom 450",
        "Symptom 232",
        "Symptom 580",
        "Symptom 311",
        "Symptom 470",
        "Symptom 592",
        "Symptom 530",
        "Symptom 4",
        "Symptom 583",
        "Symptom 253",
        "Symptom 2",
        "Symptom 26",
        "Symptom 609",
        "Symptom 529",
        "Symptom 560",
        "Symptom 273",
        "Symptom 87",
        "Symptom 116",
        "Symptom 607",
        "Symptom 159",
        "Symptom 226",
        "Symptom 509",
        "Symptom 208",
        "Symptom 571",
        "Symptom 117",
        "Symptom 7",
        "Symptom 473",
        "Symptom 568",
        "Symptom 605",
        "Symptom 118",
        "Symptom 242",
        "Symptom 486",
        "Symptom 6",
        "Symptom 327",
        "Symptom 17",
        "Symptom 314",
        "Symptom 270",
        "Symptom 382",
        "Symptom 387",
        "Symptom 312",
        "Symptom 218",
        "Symptom 84",
        "Symptom 324",
        "Symptom 107",
        "Symptom 189",
        "Symptom 236",
        "Symptom 263",
        "Symptom 472",
        "Symptom 315",
        "Symptom 491",
        "Symptom 134",
        "Symptom 121",
        "Symptom 224",
        "Symptom 474",
        "Symptom 112",
        "Symptom 126",
        "Symptom 102",
        "Symptom 563",
        "Symptom 594",
        "Symptom 404",
        "Symptom 261",
        "Symptom 418",
        "Symptom 246",
        "Symptom 238",
        "Symptom 257",
        "Symptom 276",
        "Symptom 494",
        "Symptom 13",
        "Symptom 114",
        "Symptom 70",
        "Symptom 495",
        "Symptom 296",
        "Symptom 266",
        "Symptom 37",
        "Symptom 581",
        "Symptom 220",
        "Symptom 426",
        "Symptom 499",
        "Symptom 330",
        "Symptom 283",
        "Symptom 221",
        "Symptom 142",
        "Symptom 249",
        "Symptom 589",
        "Symptom 520",
        "Symptom 8",
        "Symptom 432",
        "Symptom 184",
        "Symptom 293",
        "Symptom 245",
        "Symptom 521",
        "Symptom 559",
        "Symptom 22",
        "Symptom 217",
        "Symptom 212",
        "Symptom 310",
        "Symptom 120",
        "Symptom 585",
        "Symptom 512",
        "Symptom 487",
        "Symptom 115",
        "Symptom 269",
        "Symptom 265",
        "Symptom 222",
        "Symptom 207",
        "Symptom 437",
        "Symptom 135",
        "Symptom 223",
        "Symptom 95",
        "Symptom 235",
        "Symptom 225",
        "Symptom 469",
        "Symptom 170",
        "Symptom 258",
        "Symptom 144",
        "Symptom 157",
        "Symptom 278",
        "Symptom 405",
        "Symptom 406",
        "Symptom 119",
        "Symptom 141",
        "Symptom 291",
        "Symptom 516",
        "Symptom 351",
        "Symptom 337",
        "Symptom 326",
        "Symptom 502",
        "Symptom 74",
        "Symptom 396",
        "Symptom 511",
        "Symptom 199",
        "Symptom 439",
        "Symptom 54",
        "Symptom 572",
        "Symptom 69",
        "Symptom 59",
        "Symptom 431",
        "Symptom 444",
        "Symptom 287",
        "Symptom 98",
        "Symptom 93",
        "Symptom 381",
        "Symptom 267",
        "Symptom 252",
        "Symptom 514",
        "Symptom 113",
        "Symptom 215",
        "Symptom 256",
        "Symptom 260",
        "Symptom 564",
        "Symptom 243",
        "Symptom 419",
        "Symptom 524",
        "Symptom 181",
        "Symptom 280",
        "Symptom 197",
        "Symptom 277",
        "Symptom 268",
        "Symptom 80",
        "Symptom 371",
        "Symptom 392",
        "Symptom 27",
        "Symptom 434",
        "Symptom 417",
        "Symptom 35",
        "Symptom 285",
        "Symptom 332",
        "Symptom 79",
        "Symptom 129",
        "Symptom 155",
        "Symptom 582",
        "Symptom 415",
        "Symptom 342",
        "Symptom 429",
        "Symptom 230",
        "Symptom 308",
        "Symptom 329",
        "Symptom 289",
        "Symptom 187",
        "Symptom 284",
        "Symptom 333",
        "Symptom 10",
        "Symptom 409",
        "Symptom 359",
        "Symptom 143",
        "Symptom 272",
        "Symptom 318",
        "Symptom 522",
        "Symptom 608",
        "Symptom 240",
        "Symptom 248",
        "Symptom 517",
        "Symptom 534",
        "Symptom 452",
        "Symptom 251",
        "Symptom 338",
        "Symptom 400",
        "Symptom 440",
        "Symptom 101",
        "Symptom 340",
        "Symptom 604",
        "Symptom 441",
        "Symptom 345",
        "Symptom 147",
        "Symptom 448",
        "Symptom 410",
        "Symptom 241",
        "Symptom 158",
        "Symptom 286",
        "Symptom 171",
        "Symptom 533",
        "Symptom 203",
        "Symptom 573",
        "Symptom 532",
        "Symptom 21",
        "Symptom 137",
        "Symptom 188",
        "Symptom 125",
        "Symptom 124",
        "Symptom 210",
        "Symptom 262",
        "Symptom 175",
        "Symptom 133",
        "Symptom 475",
        "Symptom 466",
        "Symptom 109",
        "Symptom 110",
        "Symptom 271",
        "Symptom 51",
        "Symptom 544",
        "Symptom 479",
        "Symptom 462",
        "Symptom 297",
        "Symptom 449",
        "Symptom 63",
        "Symptom 104",
        "Symptom 423",
        "Symptom 390",
        "Symptom 288",
        "Symptom 19",
        "Symptom 383",
        "Symptom 430",
        "Symptom 455",
        "Symptom 443",
        "Symptom 180",
        "Symptom 45",
        "Symptom 44",
        "Symptom 89",
        "Symptom 12",
        "Symptom 229",
        "Symptom 239",
        "Symptom 317",
        "Symptom 412",
        "Symptom 411",
        "Symptom 9",
        "Symptom 595",
        "Symptom 438",
        "Symptom 264",
        "Symptom 421",
        "Symptom 172",
        "Symptom 259",
        "Symptom 169",
        "Symptom 385",
        "Symptom 127",
        "Symptom 384",
        "Symptom 506",
        "Symptom 165",
        "Symptom 247",
        "Symptom 372",
        "Symptom 75",
        "Symptom 519",
        "Symptom 465",
        "Symptom 30",
        "Symptom 105",
        "Symptom 86",
        "Symptom 374",
        "Symptom 458",
        "Symptom 526",
        "Symptom 325",
        "Symptom 15",
        "Symptom 5",
        "Symptom 23",
        "Symptom 323",
        "Symptom 501",
        "Symptom 255",
        "Symptom 587",
        "Symptom 402",
        "Symptom 403",
        "Symptom 211",
        "Symptom 156",
        "Symptom 216",
        "Symptom 453",
        "Symptom 569",
        "Symptom 373",
        "Symptom 43",
        "Symptom 106",
        "Symptom 601",
        "Symptom 459",
        "Symptom 295",
        "Symptom 435",
        "Symptom 370",
        "Symptom 65",
        "Symptom 464",
        "Symptom 468",
        "Symptom 380",
        "Symptom 352",
        "Symptom 292",
        "Symptom 454",
        "Symptom 130",
        "Symptom 301",
        "Symptom 335",
        "Symptom 33",
        "Symptom 391",
        "Symptom 358",
        "Symptom 602",
        "Symptom 294",
        "Symptom 88",
        "Symptom 205",
        "Symptom 66",
        "Symptom 94",
        "Symptom 467",
        "Symptom 456",
        "Symptom 377",
        "Symptom 537",
        "Symptom 62",
        "Symptom 274",
        "Symptom 56",
        "Symptom 316",
        "Symptom 551",
        "Symptom 313",
        "Symptom 518",
        "Symptom 375",
        "Symptom 593",
        "Symptom 510",
        "Symptom 53",
        "Symptom 183",
        "Symptom 362",
        "Symptom 34",
        "Symptom 420",
        "Symptom 376",
        "Symptom 162",
        "Symptom 305",
        "Symptom 368",
        "Symptom 361",
        "Symptom 498",
        "Symptom 209",
        "Symptom 20",
        "Symptom 600",
        "Symptom 25",
        "Symptom 531",
        "Symptom 389",
        "Symptom 596",
        "Symptom 176",
        "Symptom 515",
        "Symptom 543",
        "Symptom 461",
        "Symptom 228",
        "Symptom 250",
        "Symptom 173",
        "Symptom 177",
        "Symptom 401",
        "Symptom 457",
        "Symptom 244",
        "Symptom 508",
        "Symptom 55",
        "Symptom 290",
        "Symptom 463",
        "Symptom 553",
        "Symptom 67",
        "Symptom 99",
        "Symptom 545",
        "Symptom 397",
        "Symptom 32",
        "Symptom 186",
        "Symptom 558",
        "Symptom 227",
        "Symptom 513",
        "Symptom 198",
        "Symptom 3",
        "Symptom 148",
        "Symptom 603",
        "Symptom 136",
        "Symptom 50",
        "Symptom 48",
        "Symptom 365",
        "Symptom 77",
        "Symptom 237",
        "Symptom 303",
        "Symptom 428",
        "Symptom 578",
        "Symptom 597",
        "Symptom 182",
        "Symptom 282",
        "Symptom 47",
        "Symptom 507",
        "Symptom 174",
        "Symptom 579",
        "Symptom 485",
        "Symptom 57",
        "Symptom 14",
        "Symptom 598",
        "Symptom 492",
        "Symptom 588",
        "Symptom 379",
        "Symptom 97",
        "Symptom 497",
        "Symptom 424",
        "Symptom 503",
        "Symptom 606",
        "Symptom 233",
        "Symptom 398",
        "Symptom 548",
        "Symptom 556",
        "Symptom 574",
        "Symptom 195",
        "Symptom 275",
        "Symptom 319",
        "Symptom 213",
        "Symptom 460",
        "Symptom 281",
        "Symptom 366",
        "Symptom 504",
        "Symptom 577",
        "Symptom 92",
        "Symptom 231",
        "Symptom 178",
        "Symptom 546",
        "Symptom 550",
        "Symptom 350",
        "Symptom 154",
        "Symptom 214",
        "Symptom 535",
        "Symptom 164",
        "Symptom 254",
        "Symptom 360",
        "Symptom 552",
        "Symptom 427",
        "Symptom 11",
        "Symptom 160",
        "Symptom 131",
        "Symptom 304",
        "Symptom 557",
        "Symptom 60",
        "Symptom 194",
        "Symptom 505",
        "Symptom 416",
        "Symptom 322",
        "Symptom 71",
        "Symptom 279",
        "Symptom 321",
        "Symptom 219",
        "Symptom 328",
        "Symptom 584",
        "Symptom 42",
        "Symptom 150",
        "Symptom 408",
        "Symptom 40",
        "Symptom 193",
        "Symptom 331",
        "Symptom 185",
        "Symptom 523",
        "Symptom 356",
        "Symptom 388",
        "Symptom 540",
        "Symptom 354",
        "Symptom 566",
        "Symptom 493",
        "Symptom 433",
        "Symptom 542",
        "Symptom 425",
        "Symptom 436",
        "Symptom 586",
        "Symptom 96",
        "Symptom 536",
        "Symptom 152",
        "Symptom 555",
        "Symptom 496",
        "Symptom 500",
        "Symptom 61",
        "Symptom 488",
        "Symptom 407",
        "Symptom 348",
        "Symptom 353",
        "Symptom 151",
        "Symptom 575",
        "Symptom 234",
        "Symptom 68",
        "Symptom 320",
        "Symptom 538",
        "Symptom 29",
        "Symptom 547",
        "Symptom 111",
        "Symptom 567",
        "Symptom 167",
        "Symptom 541",
        "Symptom 590",
        "Symptom 599",
        "Symptom 528",
        "Symptom 481",
        "Symptom 355",
        "Symptom 307",
        "Symptom 364",
        "Symptom 299",
        "Symptom 309",
        "Symptom 346",
        "Symptom 357",
        "Symptom 525",
        "Symptom 58",
        "Symptom 576",
        "Symptom 483",
        "Symptom 562",
        "Symptom 190",
        "Symptom 341",
        "Symptom 570",
        "Symptom 83",
        "Symptom 179",
        "Symptom 81",
        "Symptom 73",
        "Symptom 447",
        "Symptom 103",
        "Symptom 204",
        "Symptom 565",
        "Symptom 302",
    ]
    cmdb_cis = [
        "cmdb_ci 31",
        "cmdb_ci 23",
        "cmdb_ci 22",
        "cmdb_ci 6",
        "cmdb_ci 3",
        "cmdb_ci 49",
        "cmdb_ci 15",
        "cmdb_ci 16",
        "cmdb_ci 19",
        "cmdb_ci 48",
        "cmdb_ci 14",
        "cmdb_ci 28",
        "cmdb_ci 21",
        "cmdb_ci 11",
        "cmdb_ci 10",
        "cmdb_ci 2",
        "cmdb_ci 7",
        "cmdb_ci 5",
        "cmdb_ci 12",
        "cmdb_ci 35",
        "cmdb_ci 26",
        "cmdb_ci 53",
        "cmdb_ci 4",
        "cmdb_ci 17",
        "cmdb_ci 51",
        "cmdb_ci 33",
        "cmdb_ci 36",
        "cmdb_ci 13",
        "cmdb_ci 27",
        "cmdb_ci 8",
        "cmdb_ci 9",
        "cmdb_ci 42",
        "cmdb_ci 39",
        "cmdb_ci 34",
        "cmdb_ci 24",
        "cmdb_ci 46",
        "cmdb_ci 47",
        "cmdb_ci 41",
        "cmdb_ci 38",
        "cmdb_ci 20",
        "cmdb_ci 50",
        "cmdb_ci 40",
        "cmdb_ci 18",
        "cmdb_ci 37",
        "cmdb_ci 45",
        "cmdb_ci 32",
        "cmdb_ci 43",
        "cmdb_ci 29",
        "cmdb_ci 30",
        "cmdb_ci 25",
    ]
    groups = [
        "Group 56",
        "Group 70",
        "Group 24",
        "Group 25",
        "Group 23",
        "Group 28",
        "Group 5",
        "Group 15",
        "Group 12",
        "Group 33",
        "Group 54",
        "Group 29",
        "Group 66",
        "Group 65",
        "Group 68",
        "Group 58",
        "Group 27",
        "Group 72",
        "Group 30",
        "Group 50",
        "Group 55",
        "Group 62",
        "Group 47",
        "Group 22",
        "Group 39",
        "Group 73",
        "Group 20",
        "Group 46",
        "Group 67",
        "Group 74",
        "Group 34",
        "Group 69",
        "Group 3",
        "Group 31",
        "Group 26",
        "Group 53",
        "Group 76",
        "Group 6",
        "Group 61",
        "Group 57",
        "Group 37",
        "Group 48",
        "Group 17",
        "Group 49",
        "Group 43",
        "Group 60",
        "Group 10",
        "Group 9",
        "Group 45",
        "Group 14",
        "Group 59",
        "Group 64",
        "Group 51",
        "Group 75",
        "Group 11",
        "Group 19",
        "Group 21",
        "Group 77",
        "Group 2",
        "Group 13",
        "Group 35",
        "Group 81",
        "Group 44",
        "Group 63",
        "Group 79",
        "Group 32",
        "Group 78",
        "Group 36",
        "Group 82",
        "Group 80",
        "Group 4",
        "Group 71",
        "Group 18",
        "Group 38",
        "Group 16",
        "Group 41",
        "Group 7",
        "Group 8",
    ]
    problem_ids = [
        "Problem ID  2",
        "Problem ID  4",
        "Problem ID  44",
        "Problem ID  141",
        "Problem ID  5",
        "Problem ID  17",
        "Problem ID  23",
        "Problem ID  20",
        "Problem ID  19",
        "Problem ID  24",
        "Problem ID  12",
        "Problem ID  6",
        "Problem ID  7",
        "Problem ID  10",
        "Problem ID  40",
        "Problem ID  33",
        "Problem ID  26",
        "Problem ID  15",
        "Problem ID  9",
        "Problem ID  8",
        "Problem ID  14",
        "Problem ID  18",
        "Problem ID  11",
        "Problem ID  72",
        "Problem ID  246",
        "Problem ID  16",
        "Problem ID  21",
        "Problem ID  28",
        "Problem ID  74",
        "Problem ID  35",
        "Problem ID  104",
        "Problem ID  27",
        "Problem ID  51",
        "Problem ID  30",
        "Problem ID  29",
        "Problem ID  3",
        "Problem ID  31",
        "Problem ID  45",
        "Problem ID  32",
        "Problem ID  38",
        "Problem ID  91",
        "Problem ID  13",
        "Problem ID  36",
        "Problem ID  46",
        "Problem ID  84",
        "Problem ID  39",
        "Problem ID  70",
        "Problem ID  41",
        "Problem ID  118",
        "Problem ID  42",
        "Problem ID  83",
        "Problem ID  43",
        "Problem ID  48",
        "Problem ID  71",
        "Problem ID  68",
        "Problem ID  92",
        "Problem ID  47",
        "Problem ID  192",
        "Problem ID  103",
        "Problem ID  99",
        "Problem ID  85",
        "Problem ID  219",
        "Problem ID  50",
        "Problem ID  49",
        "Problem ID  57",
        "Problem ID  82",
        "Problem ID  52",
        "Problem ID  81",
        "Problem ID  53",
        "Problem ID  54",
        "Problem ID  55",
        "Problem ID  56",
        "Problem ID  80",
        "Problem ID  59",
        "Problem ID  58",
        "Problem ID  96",
        "Problem ID  62",
        "Problem ID  79",
        "Problem ID  69",
        "Problem ID  60",
        "Problem ID  64",
        "Problem ID  63",
        "Problem ID  65",
        "Problem ID  78",
        "Problem ID  77",
        "Problem ID  66",
        "Problem ID  67",
        "Problem ID  76",
        "Problem ID  75",
        "Problem ID  73",
        "Problem ID  86",
        "Problem ID  93",
        "Problem ID  100",
        "Problem ID  94",
        "Problem ID  87",
        "Problem ID  89",
        "Problem ID  88",
        "Problem ID  90",
        "Problem ID  95",
        "Problem ID  97",
        "Problem ID  61",
        "Problem ID  22",
        "Problem ID  144",
        "Problem ID  98",
        "Problem ID  240",
        "Problem ID  114",
        "Problem ID  101",
        "Problem ID  102",
        "Problem ID  106",
        "Problem ID  105",
        "Problem ID  130",
        "Problem ID  115",
        "Problem ID  107",
        "Problem ID  218",
        "Problem ID  158",
        "Problem ID  116",
        "Problem ID  109",
        "Problem ID  108",
        "Problem ID  112",
        "Problem ID  111",
        "Problem ID  110",
        "Problem ID  113",
        "Problem ID  169",
        "Problem ID  146",
        "Problem ID  119",
        "Problem ID  121",
        "Problem ID  120",
        "Problem ID  117",
        "Problem ID  154",
        "Problem ID  131",
        "Problem ID  206",
        "Problem ID  124",
        "Problem ID  123",
        "Problem ID  125",
        "Problem ID  122",
        "Problem ID  126",
        "Problem ID  127",
        "Problem ID  128",
        "Problem ID  139",
        "Problem ID  138",
        "Problem ID  25",
        "Problem ID  181",
        "Problem ID  129",
        "Problem ID  142",
        "Problem ID  133",
        "Problem ID  132",
        "Problem ID  134",
        "Problem ID  165",
        "Problem ID  135",
        "Problem ID  136",
        "Problem ID  137",
        "Problem ID  143",
        "Problem ID  140",
        "Problem ID  145",
        "Problem ID  148",
        "Problem ID  151",
        "Problem ID  162",
        "Problem ID  147",
        "Problem ID  149",
        "Problem ID  152",
        "Problem ID  150",
        "Problem ID  157",
        "Problem ID  156",
        "Problem ID  153",
        "Problem ID  190",
        "Problem ID  250",
        "Problem ID  155",
        "Problem ID  164",
        "Problem ID  199",
        "Problem ID  231",
        "Problem ID  163",
        "Problem ID  159",
        "Problem ID  161",
        "Problem ID  160",
        "Problem ID  174",
        "Problem ID  166",
        "Problem ID  167",
        "Problem ID  172",
        "Problem ID  173",
        "Problem ID  168",
        "Problem ID  170",
        "Problem ID  210",
        "Problem ID  179",
        "Problem ID  171",
        "Problem ID  184",
        "Problem ID  187",
        "Problem ID  175",
        "Problem ID  176",
        "Problem ID  177",
        "Problem ID  202",
        "Problem ID  178",
        "Problem ID  188",
        "Problem ID  180",
        "Problem ID  182",
        "Problem ID  185",
        "Problem ID  183",
        "Problem ID  189",
        "Problem ID  186",
        "Problem ID  200",
        "Problem ID  193",
        "Problem ID  191",
        "Problem ID  198",
        "Problem ID  220",
        "Problem ID  195",
        "Problem ID  201",
        "Problem ID  225",
        "Problem ID  196",
        "Problem ID  197",
        "Problem ID  213",
        "Problem ID  204",
        "Problem ID  194",
        "Problem ID  203",
        "Problem ID  205",
        "Problem ID  243",
        "Problem ID  207",
        "Problem ID  208",
        "Problem ID  228",
        "Problem ID  209",
        "Problem ID  211",
        "Problem ID  212",
        "Problem ID  245",
        "Problem ID  214",
        "Problem ID  223",
        "Problem ID  215",
        "Problem ID  216",
        "Problem ID  217",
        "Problem ID  229",
        "Problem ID  221",
        "Problem ID  222",
        "Problem ID  226",
        "Problem ID  224",
        "Problem ID  230",
        "Problem ID  227",
        "Problem ID  235",
        "Problem ID  242",
        "Problem ID  232",
        "Problem ID  233",
        "Problem ID  234",
        "Problem ID  236",
        "Problem ID  237",
        "Problem ID  238",
        "Problem ID  239",
        "Problem ID  241",
        "Problem ID  248",
        "Problem ID  247",
        "Problem ID  249",
        "Problem ID  252",
        "Problem ID  253",
        "Problem ID  256",
        "Problem ID  255",
        "Problem ID  251",
        "Problem ID  259",
    ]

    def _random_timestamp():
        return datetime.utcnow() - timedelta(
            days=np.random.randint(0, 3), seconds=np.random.randint(0, 1e6)
        )

    return {
        "reassignment_count": np.random.randint(0, 10),
        "reopen_count": np.random.randint(0, 3),
        "sys_mod_count": np.random.randint(0, 10),
        "opened_at": _random_timestamp().strftime("%d/%m/%Y %H:%M"),
        "sys_created_at": _random_timestamp().strftime("%d/%m/%Y %H:%M"),
        "sys_updated_at": _random_timestamp().strftime("%d/%m/%Y %H:%M"),
        "u_priority_confirmation": bool(np.random.choice([True, False], 1, p=[0.28, 0.72])[0]),
        "contact_type": np.random.choice(
            ["Phone", "Email", "Self service", "Direct opening", "IVR"],
            1,
            p=[0.4, 0.3, 0.15, 0.1, 0.05],
        )[0],
        "location": np.random.choice(locations, 1)[0],
        "category": np.random.choice(categories, 1)[0],
        "subcategory": np.random.choice(subcategories, 1)[0],
        "u_symptom": np.random.choice(symptoms, 1)[0],
        "cmdb_ci": np.random.choice(cmdb_cis, 1)[0],
        "impact": np.random.choice(["2 - Medium", "1 - High", "3 - Low"], 1)[0],
        "urgency": np.random.choice(["2 - Medium", "1 - High", "3 - Low"], 1)[0],
        "priority": np.random.choice(["3 - Moderate", "2 - High", "4 - Low", "1 - Critical"], 1)[0],
        "assignment_group": np.random.choice(groups, 1)[0],
        "notify": np.random.choice(["Do Not Notify", "Send Email"], 1, p=[0.98, 0.02])[0],
        "problem_id": np.random.choice(problem_ids, 1)[0],
    }


if __name__ == "__main__":
    num_records = int(sys.argv[1])
    out = {"data": [_get_one_record() for i in range(num_records)]}
    sys.stdout.write(json.dumps(out))
