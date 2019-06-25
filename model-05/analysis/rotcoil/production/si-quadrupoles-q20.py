#!/usr/bin/env python-sirius
"""."""

import numpy as np
import matplotlib.pyplot as plt
from lnls import rotcoil as r



RotCoilMeas = r.RotCoilMeas_SIQuadQ20


qfa = {
    'SI-01M2:MA-QFA': 'Q20-076',
    'SI-05M1:MA-QFA': 'Q20-079',
    'SI-05M2:MA-QFA': 'Q20-176',
    'SI-09M1:MA-QFA': 'Q20-074',
    'SI-09M2:MA-QFA': 'Q20-101',
    'SI-13M1:MA-QFA': 'Q20-162',
    'SI-13M2:MA-QFA': 'Q20-155',
    'SI-17M1:MA-QFA': 'Q20-095',
    'SI-17M2:MA-QFA': 'Q20-071',
    'SI-01M1:MA-QFA': 'Q20-049',
}

q1 = {
    'SI-01C1:MA-Q1': 'Q20-030',
    'SI-01C4:MA-Q1': 'Q20-132',
    'SI-02C1:MA-Q1': 'Q20-013',
    'SI-02C4:MA-Q1': 'Q20-014',
    'SI-03C1:MA-Q1': 'Q20-027',
    'SI-03C4:MA-Q1': 'Q20-008',
    'SI-04C1:MA-Q1': 'Q20-029',
    'SI-04C4:MA-Q1': 'Q20-023',
    'SI-05C1:MA-Q1': 'Q20-149',
    'SI-05C4:MA-Q1': 'Q20-028',
    'SI-06C1:MA-Q1': 'Q20-036',
    'SI-06C4:MA-Q1': 'Q20-033',
    'SI-07C1:MA-Q1': 'Q20-020',
    'SI-07C4:MA-Q1': 'Q20-015',
    'SI-08C1:MA-Q1': 'Q20-125',
    'SI-08C4:MA-Q1': 'Q20-153',
    'SI-09C1:MA-Q1': 'Q20-025',
    'SI-09C4:MA-Q1': 'Q20-067',
    'SI-10C1:MA-Q1': 'Q20-035',
    'SI-10C4:MA-Q1': 'Q20-141',
    'SI-11C1:MA-Q1': 'Q20-119',
    'SI-11C4:MA-Q1': 'Q20-012',
    'SI-12C1:MA-Q1': 'Q20-111',
    'SI-12C4:MA-Q1': 'Q20-006',
    'SI-13C1:MA-Q1': 'Q20-164',
    'SI-13C4:MA-Q1': 'Q20-024',
    'SI-14C1:MA-Q1': 'Q20-010',
    'SI-14C4:MA-Q1': 'Q20-032',
    'SI-15C1:MA-Q1': 'Q20-011',
    'SI-15C4:MA-Q1': 'Q20-005',
    'SI-16C1:MA-Q1': 'Q20-039',
    'SI-16C4:MA-Q1': 'Q20-109',
    'SI-17C1:MA-Q1': 'Q20-016',
    'SI-17C4:MA-Q1': 'Q20-009',
    'SI-18C1:MA-Q1': 'Q20-026',
    'SI-18C4:MA-Q1': 'Q20-037',
    'SI-19C1:MA-Q1': 'Q20-038',
    'SI-19C4:MA-Q1': 'Q20-017',
    'SI-20C1:MA-Q1': 'Q20-007',
    'SI-20C4:MA-Q1': 'Q20-021',
}

q2 = {
    'SI-01C1:MA-Q2': 'Q20-096',
    'SI-01C4:MA-Q2': 'Q20-034',
    'SI-02C1:MA-Q2': 'Q20-092',
    'SI-02C4:MA-Q2': 'Q20-122',
    'SI-03C1:MA-Q2': 'Q20-136',
    'SI-03C4:MA-Q2': 'Q20-174',
    'SI-04C1:MA-Q2': 'Q20-056',
    'SI-04C4:MA-Q2': 'Q20-059',
    'SI-05C1:MA-Q2': 'Q20-128',
    'SI-05C4:MA-Q2': 'Q20-115',
    'SI-06C1:MA-Q2': 'Q20-126',
    'SI-06C4:MA-Q2': 'Q20-158',
    'SI-07C1:MA-Q2': 'Q20-073',
    'SI-07C4:MA-Q2': 'Q20-087',
    'SI-08C1:MA-Q2': 'Q20-137',
    'SI-08C4:MA-Q2': 'Q20-082',
    'SI-09C1:MA-Q2': 'Q20-050',
    'SI-09C4:MA-Q2': 'Q20-117',
    'SI-10C1:MA-Q2': 'Q20-105',
    'SI-10C4:MA-Q2': 'Q20-124',
    'SI-11C1:MA-Q2': 'Q20-120',
    'SI-11C4:MA-Q2': 'Q20-118',
    'SI-12C1:MA-Q2': 'Q20-134',
    'SI-12C4:MA-Q2': 'Q20-135',
    'SI-13C1:MA-Q2': 'Q20-068',
    'SI-13C4:MA-Q2': 'Q20-098',
    'SI-14C1:MA-Q2': 'Q20-072',
    'SI-14C4:MA-Q2': 'Q20-175',
    'SI-15C1:MA-Q2': 'Q20-178',
    'SI-15C4:MA-Q2': 'Q20-104',
    'SI-16C1:MA-Q2': 'Q20-046',
    'SI-16C4:MA-Q2': 'Q20-154',
    'SI-17C1:MA-Q2': 'Q20-167',
    'SI-17C4:MA-Q2': 'Q20-094',
    'SI-18C1:MA-Q2': 'Q20-062',
    'SI-18C4:MA-Q2': 'Q20-102',
    'SI-19C1:MA-Q2': 'Q20-131',
    'SI-19C4:MA-Q2': 'Q20-138',
    'SI-20C1:MA-Q2': 'Q20-065',
    'SI-20C4:MA-Q2': 'Q20-152',
}


q3 = {
    'SI-01C2:MA-Q3': 'Q20-066',
    'SI-01C3:MA-Q3': 'Q20-061',
    'SI-02C2:MA-Q3': 'Q20-091',
    'SI-02C3:MA-Q3': 'Q20-004',
    'SI-03C2:MA-Q3': 'Q20-147',
    'SI-03C3:MA-Q3': 'Q20-114',
    'SI-04C2:MA-Q3': 'Q20-112',
    'SI-04C3:MA-Q3': 'Q20-165',
    'SI-05C2:MA-Q3': 'Q20-107',
    'SI-05C3:MA-Q3': 'Q20-019',
    'SI-06C2:MA-Q3': 'Q20-179',
    'SI-06C3:MA-Q3': 'Q20-106',
    'SI-07C2:MA-Q3': 'Q20-148',
    'SI-07C3:MA-Q3': 'Q20-108',
    'SI-08C2:MA-Q3': 'Q20-070',
    'SI-08C3:MA-Q3': 'Q20-159',
    'SI-09C2:MA-Q3': 'Q20-121',
    'SI-09C3:MA-Q3': 'Q20-045',
    'SI-10C2:MA-Q3': 'Q20-042',
    'SI-10C3:MA-Q3': 'Q20-130',
    'SI-11C2:MA-Q3': 'Q20-161',
    'SI-11C3:MA-Q3': 'Q20-075',
    'SI-12C2:MA-Q3': 'Q20-127',
    'SI-12C3:MA-Q3': 'Q20-022',
    'SI-13C2:MA-Q3': 'Q20-145',
    'SI-13C3:MA-Q3': 'Q20-133',
    'SI-14C2:MA-Q3': 'Q20-172',
    'SI-14C3:MA-Q3': 'Q20-129',
    'SI-15C2:MA-Q3': 'Q20-018',
    'SI-15C3:MA-Q3': 'Q20-142',
    'SI-16C2:MA-Q3': 'Q20-139',
    'SI-16C3:MA-Q3': 'Q20-113',
    'SI-17C2:MA-Q3': 'Q20-140',
    'SI-17C3:MA-Q3': 'Q20-170',
    'SI-18C2:MA-Q3': 'Q20-110',
    'SI-18C3:MA-Q3': 'Q20-044',
    'SI-19C2:MA-Q3': 'Q20-086',
    'SI-19C3:MA-Q3': 'Q20-177',
    'SI-20C2:MA-Q3': 'Q20-031',
    'SI-20C3:MA-Q3': 'Q20-064',
}

q4 = {
    'SI-01C2:MA-Q4': 'Q20-081',
    'SI-01C3:MA-Q4': 'Q20-097',
    'SI-02C2:MA-Q4': 'Q20-051',
    'SI-02C3:MA-Q4': 'Q20-168',
    'SI-03C2:MA-Q4': 'Q20-166',
    'SI-03C3:MA-Q4': 'Q20-043',
    'SI-04C2:MA-Q4': 'Q20-080',
    'SI-04C3:MA-Q4': 'Q20-047',
    'SI-05C2:MA-Q4': 'Q20-163',
    'SI-05C3:MA-Q4': 'Q20-048',
    'SI-06C2:MA-Q4': 'Q20-103',
    'SI-06C3:MA-Q4': 'Q20-116',
    'SI-07C2:MA-Q4': 'Q20-089',
    'SI-07C3:MA-Q4': 'Q20-077',
    'SI-08C2:MA-Q4': 'Q20-093',
    'SI-08C3:MA-Q4': 'Q20-063',
    'SI-09C2:MA-Q4': 'Q20-100',
    'SI-09C3:MA-Q4': 'Q20-054',
    'SI-10C2:MA-Q4': 'Q20-156',
    'SI-10C3:MA-Q4': 'Q20-169',
    'SI-11C2:MA-Q4': 'Q20-057',
    'SI-11C3:MA-Q4': 'Q20-058',
    'SI-12C2:MA-Q4': 'Q20-090',
    'SI-12C3:MA-Q4': 'Q20-150',
    'SI-13C2:MA-Q4': 'Q20-144',
    'SI-13C3:MA-Q4': 'Q20-085',
    'SI-14C2:MA-Q4': 'Q20-052',
    'SI-14C3:MA-Q4': 'Q20-069',
    'SI-15C2:MA-Q4': 'Q20-123',
    'SI-15C3:MA-Q4': 'Q20-084',
    'SI-16C2:MA-Q4': 'Q20-143',
    'SI-16C3:MA-Q4': 'Q20-171',
    'SI-17C2:MA-Q4': 'Q20-053',
    'SI-17C3:MA-Q4': 'Q20-157',
    'SI-18C2:MA-Q4': 'Q20-078',
    'SI-18C3:MA-Q4': 'Q20-146',
    'SI-19C2:MA-Q4': 'Q20-060',
    'SI-19C3:MA-Q4': 'Q20-160',
    'SI-20C2:MA-Q4': 'Q20-173',
    'SI-20C3:MA-Q4': 'Q20-083',
}


def select_dataset(serial):
    """."""
    data = RotCoilMeas(serial)
    maxc_idx = data.get_max_current_index()
    data = data.get_data_set_measurements('M1')
    return data[maxc_idx]


def get_serials(magnet_family):
    """."""
    serials = []
    for magnet in magnet_family:
        serial = magnet_family[magnet]
        serials.append(serial.replace('Q20-', ''))
    return serials


def get_analysis_data(family):
    """."""
    serials = get_serials(family)
    current = []
    xcenter = []
    ycenter = []
    quadrupole = []
    roterror = []
    for serial in serials:
        data = select_dataset(serial)
        c = data.main_coil_current_avg
        h = data.harmonics
        main_idx = h.index(RotCoilMeas.main_harmonic)
        x = data.magnetic_center_x
        y = data.magnetic_center_y
        n = data.intmpole_normal_avg[main_idx]
        s = data.intmpole_skew_avg[main_idx]
        e = data.rotation_error
        current.append(c)
        xcenter.append(x)
        ycenter.append(y)
        quadrupole.append(n)
        roterror.append(e)
        sfmt = '{}  {:.3f} A  {:+.4f} T  {:+5.1f} um  {:+5.1f} um  {:06.3f}'
        print(sfmt.format(serial, c, n, x, y, e))

    q = np.array(quadrupole)
    m, s, maxmin = np.mean(q), np.std(q), np.max(q) - np.min(q)
    print('- integrated quadrupole [T]: {:+.4f} ± {:.4f} ({:.3f} %), maxmin: {:.4f} ({:.3f} %)'.format(m, s, 100*s/m, maxmin, 100*maxmin/m))
    x = np.array(xcenter)
    m, s, maxmin = np.mean(x), np.std(x), np.max(x) - np.min(x)
    print('- xcenter [um]:               {:+.1f} ± {:.1f}, maxmin: {:.1f}'.format(m, s, maxmin))
    y = np.array(ycenter)
    m, s, maxmin = np.mean(y), np.std(y), np.max(y) - np.min(y)
    print('- ycenter [um]:               {:+.1f} ± {:.1f}, maxmin: {:.1f}'.format(m, s, maxmin))
    e = np.array(roterror)
    m, s, maxmin = np.mean(e), np.std(e), np.max(e) - np.min(e)
    print('- rotation error [mrad]:      {:+.1f} ± {:.1f}, maxmin: {:.1f} '.format(m, s, maxmin))
    print('')
    return serials, current, quadrupole, xcenter, ycenter, roterror



fams = [qfa, q1, q2, q3, q4]



def plot_integrated_quadrupole():
    """."""

    n = 0
    serials = []

    label = 'QFA'
    print(label)
    serials0, current0, quadrupole0, xcenter0, ycenter0, roterror0 = \
        get_analysis_data(fams[0])
    plt.plot(len(serials) + np.arange(len(serials0)), quadrupole0, 'b-')
    plt.plot(len(serials) + np.arange(len(serials0)), quadrupole0, 'bo', label=label)
    avg0 = np.mean(quadrupole0)
    plt.plot(len(serials) + np.arange(len(serials0)),
            [avg0, ]*len(quadrupole0), '--b')
    serials += serials0

    label = 'Q1'
    print(label)
    serials1, current1, quadrupole1, xcenter1, ycenter1, roterror1 = \
        get_analysis_data(fams[1])
    plt.plot(len(serials) + np.arange(len(serials1)), quadrupole1, 'g-')
    plt.plot(len(serials) + np.arange(len(serials1)), quadrupole1, 'go', label=label)
    avg1 = np.mean(quadrupole1)
    plt.plot(len(serials) + np.arange(len(serials1)),
            [avg1, ]*len(quadrupole1), '--g')
    serials += serials1

    label = 'Q2'
    print(label)
    serials2, current2, quadrupole2, xcenter2, ycenter2, roterror2 = \
        get_analysis_data(fams[2])
    plt.plot(len(serials) + np.arange(len(serials2)), quadrupole2, 'r-')
    plt.plot(len(serials) + np.arange(len(serials2)),
             quadrupole2, 'ro', label=label)
    avg2 = np.mean(quadrupole2)
    plt.plot(len(serials) + np.arange(len(serials2)),
            [avg2, ]*len(quadrupole2), '--r')
    serials += serials2

    label = 'Q3'
    print(label)
    serials3, current3, quadrupole3, xcenter3, ycenter3, roterror3 = \
        get_analysis_data(fams[3])
    plt.plot(len(serials) + np.arange(len(serials3)), quadrupole3, 'k-')
    plt.plot(len(serials) + np.arange(len(serials3)),
             quadrupole3, 'ko', label=label)
    avg3 = np.mean(quadrupole3)
    plt.plot(len(serials) + np.arange(len(serials3)),
            [avg3, ]*len(quadrupole3), '--k')
    serials += serials3

    label = 'Q4'
    print(label)
    serials4, current4, quadrupole4, xcenter4, ycenter4, roterror4 = \
        get_analysis_data(fams[4])
    plt.plot(len(serials) + np.arange(len(serials4)), quadrupole4, 'y-')
    plt.plot(len(serials) + np.arange(len(serials4)),
             quadrupole4, 'yo', label=label)
    avg4 = np.mean(quadrupole4)
    plt.plot(len(serials) + np.arange(len(serials4)),
            [avg4, ]*len(quadrupole4), '--y')
    serials += serials4


    # plt.xlabel('Serial Number')
    plt.xlabel('Magnet Index')
    plt.ylabel('Integrated Quadrupole [T]')
    plt.title('Q20 Integrated Quadrupoles ({:+.2f} A)'.format(np.mean(current0)))
    # plt.xticks(np.arange(len(serials)), serials, rotation='vertical')
    plt.legend()
    plt.grid()
    plt.show()


def plot_xcenter():
    """."""

    n = 0
    serials = []

    label = 'QFA'
    print(label)
    serials0, current0, quadrupole0, xcenter0, ycenter0, roterror0 = \
        get_analysis_data(fams[0])
    plt.plot(len(serials) + np.arange(len(serials0)), xcenter0, 'b-')
    plt.plot(len(serials) + np.arange(len(serials0)),
             xcenter0, 'bo', label=label)
    avg0 = np.mean(xcenter0)
    plt.plot(len(serials) + np.arange(len(serials0)),
             [avg0, ]*len(xcenter0), '--b')
    serials += serials0

    label = 'Q1'
    print(label)
    serials1, current1, quadrupole1, xcenter1, ycenter1, roterror1 = \
        get_analysis_data(fams[1])
    plt.plot(len(serials) + np.arange(len(serials1)), xcenter1, 'g-')
    plt.plot(len(serials) + np.arange(len(serials1)),
             xcenter1, 'go', label=label)
    avg1 = np.mean(xcenter1)
    plt.plot(len(serials) + np.arange(len(serials1)),
             [avg1, ]*len(xcenter1), '--g')
    serials += serials1

    label = 'Q2'
    print(label)
    serials2, current2, quadrupole2, xcenter2, ycenter2, roterror2 = \
        get_analysis_data(fams[2])
    plt.plot(len(serials) + np.arange(len(serials2)), xcenter2, 'r-')
    plt.plot(len(serials) + np.arange(len(serials2)),
             xcenter2, 'ro', label=label)
    avg2 = np.mean(xcenter2)
    plt.plot(len(serials) + np.arange(len(serials2)),
             [avg2, ]*len(xcenter2), '--r')
    serials += serials2

    label = 'Q3'
    print(label)
    serials3, current3, quadrupole3, xcenter3, ycenter3, roterror3 = \
        get_analysis_data(fams[3])
    plt.plot(len(serials) + np.arange(len(serials3)), xcenter3, 'k-')
    plt.plot(len(serials) + np.arange(len(serials3)),
             xcenter3, 'ko', label=label)
    avg3 = np.mean(xcenter3)
    plt.plot(len(serials) + np.arange(len(serials3)),
             [avg3, ]*len(xcenter3), '--k')
    serials += serials3

    label = 'Q4'
    print(label)
    serials4, current4, quadrupole4, xcenter4, ycenter4, roterror4 = \
        get_analysis_data(fams[4])
    plt.plot(len(serials) + np.arange(len(serials4)), xcenter4, 'y-')
    plt.plot(len(serials) + np.arange(len(serials4)),
             xcenter4, 'yo', label=label)
    avg4 = np.mean(xcenter4)
    plt.plot(len(serials) + np.arange(len(serials4)),
             [avg4, ]*len(xcenter4), '--y')
    serials += serials4

    # plt.xlabel('Serial Number')
    plt.xlabel('Magnet Index')
    plt.ylabel('Magnetic Center [um]')
    plt.title(
        'Q20 Horizontal Magnetic Center ({:+.2f} A)'.format(np.mean(current0)))
    # plt.xticks(np.arange(len(serials)), serials, rotation='vertical')
    plt.legend()
    plt.grid()
    plt.show()


def plot_ycenter():
    """."""

    n = 0
    serials = []

    label = 'QFA'
    print(label)
    serials0, current0, quadrupole0, xcenter0, ycenter0, roterror0 = \
        get_analysis_data(fams[0])
    plt.plot(len(serials) + np.arange(len(serials0)), ycenter0, 'b-')
    plt.plot(len(serials) + np.arange(len(serials0)),
             ycenter0, 'bo', label=label)
    avg0 = np.mean(ycenter0)
    plt.plot(len(serials) + np.arange(len(serials0)),
             [avg0, ]*len(ycenter0), '--b')
    serials += serials0

    label = 'Q1'
    print(label)
    serials1, current1, quadrupole1, xcenter1, ycenter1, roterror1 = \
        get_analysis_data(fams[1])
    plt.plot(len(serials) + np.arange(len(serials1)), ycenter1, 'g-')
    plt.plot(len(serials) + np.arange(len(serials1)),
             ycenter1, 'go', label=label)
    avg1 = np.mean(ycenter1)
    plt.plot(len(serials) + np.arange(len(serials1)),
             [avg1, ]*len(ycenter1), '--g')
    serials += serials1

    label = 'Q2'
    print(label)
    serials2, current2, quadrupole2, xcenter2, ycenter2, roterror2 = \
        get_analysis_data(fams[2])
    plt.plot(len(serials) + np.arange(len(serials2)), ycenter2, 'r-')
    plt.plot(len(serials) + np.arange(len(serials2)),
             ycenter2, 'ro', label=label)
    avg2 = np.mean(ycenter2)
    plt.plot(len(serials) + np.arange(len(serials2)),
             [avg2, ]*len(ycenter2), '--r')
    serials += serials2

    label = 'Q3'
    print(label)
    serials3, current3, quadrupole3, xcenter3, ycenter3, roterror3 = \
        get_analysis_data(fams[3])
    plt.plot(len(serials) + np.arange(len(serials3)), ycenter3, 'k-')
    plt.plot(len(serials) + np.arange(len(serials3)),
             ycenter3, 'ko', label=label)
    avg3 = np.mean(ycenter3)
    plt.plot(len(serials) + np.arange(len(serials3)),
             [avg3, ]*len(ycenter3), '--k')
    serials += serials3

    label = 'Q4'
    print(label)
    serials4, current4, quadrupole4, xcenter4, ycenter4, roterror4 = \
        get_analysis_data(fams[4])
    plt.plot(len(serials) + np.arange(len(serials4)), ycenter4, 'y-')
    plt.plot(len(serials) + np.arange(len(serials4)),
             ycenter4, 'yo', label=label)
    avg4 = np.mean(ycenter4)
    plt.plot(len(serials) + np.arange(len(serials4)),
             [avg4, ]*len(ycenter4), '--y')
    serials += serials4

    # plt.xlabel('Serial Number')
    plt.xlabel('Magnet Index')
    plt.ylabel('Magnetic Center [um]')
    plt.title(
        'Q20 Vertical Magnetic Center ({:+.2f} A)'.format(np.mean(current0)))
    # plt.xticks(np.arange(len(serials)), serials, rotation='vertical')
    plt.legend()
    plt.grid()
    plt.show()


def plot_roterror():
    """."""

    n = 0
    serials = []

    label = 'QFA'
    print(label)
    serials0, current0, quadrupole0, xcenter0, ycenter0, roterror0 = \
        get_analysis_data(fams[0])
    plt.plot(len(serials) + np.arange(len(serials0)), roterror0, 'b-')
    plt.plot(len(serials) + np.arange(len(serials0)),
             roterror0, 'bo', label=label)
    avg0 = np.mean(roterror0)
    plt.plot(len(serials) + np.arange(len(serials0)),
             [avg0, ]*len(roterror0), '--b')
    serials += serials0

    label = 'Q1'
    print(label)
    serials1, current1, quadrupole1, xcenter1, ycenter1, roterror1 = \
        get_analysis_data(fams[1])
    plt.plot(len(serials) + np.arange(len(serials1)), roterror1, 'g-')
    plt.plot(len(serials) + np.arange(len(serials1)),
             roterror1, 'go', label=label)
    avg1 = np.mean(roterror1)
    plt.plot(len(serials) + np.arange(len(serials1)),
             [avg1, ]*len(roterror1), '--g')
    serials += serials1

    label = 'Q2'
    print(label)
    serials2, current2, quadrupole2, xcenter2, ycenter2, roterror2 = \
        get_analysis_data(fams[2])
    plt.plot(len(serials) + np.arange(len(serials2)), roterror2, 'r-')
    plt.plot(len(serials) + np.arange(len(serials2)),
             roterror2, 'ro', label=label)
    avg2 = np.mean(roterror2)
    plt.plot(len(serials) + np.arange(len(serials2)),
             [avg2, ]*len(roterror2), '--r')
    serials += serials2

    label = 'Q3'
    print(label)
    serials3, current3, quadrupole3, xcenter3, ycenter3, roterror3 = \
        get_analysis_data(fams[3])
    plt.plot(len(serials) + np.arange(len(serials3)), roterror3, 'k-')
    plt.plot(len(serials) + np.arange(len(serials3)),
             roterror3, 'ko', label=label)
    avg3 = np.mean(roterror3)
    plt.plot(len(serials) + np.arange(len(serials3)),
             [avg3, ]*len(roterror3), '--k')
    serials += serials3

    label = 'Q4'
    print(label)
    serials4, current4, quadrupole4, xcenter4, ycenter4, roterror4 = \
        get_analysis_data(fams[4])
    plt.plot(len(serials) + np.arange(len(serials4)), roterror4, 'y-')
    plt.plot(len(serials) + np.arange(len(serials4)),
             roterror4, 'yo', label=label)
    avg4 = np.mean(roterror4)
    plt.plot(len(serials) + np.arange(len(serials4)),
             [avg4, ]*len(roterror4), '--y')
    serials += serials4

    # plt.xlabel('Serial Number')
    plt.xlabel('Magnet Index')
    plt.ylabel('Roll error [mrad]')
    plt.title(
        'Q20 Rotation Error ({:+.2f} A)'.format(np.mean(current0)))
    # plt.xticks(np.arange(len(serials)), serials, rotation='vertical')
    plt.legend()
    plt.grid()
    plt.show()



plot_integrated_quadrupole()
plot_xcenter()
plot_ycenter()
plot_roterror()
