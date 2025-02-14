import numpy as np

rest_poses_dict = {
    "ur5": {
        "standard": np.array(
            [
                0.00,  # world_joint         (fixed)
                0.166827,  # base_joint       (revolute)
                -2.16515,  # shoulder_joint  (revolute)
                -1.64365,  # elbow_joint     (revolute)
                -0.90317,  # wrist_1_joint   (revolute)
                1.57315,  # wrist_2_joint    (revolute)
                1.74001,  # wrist_3_joint    (revolute)
                0.00,  # ee_joint            (fixed)
                0.00,  # tactip_ee_joint     (fixed)
                0.00,  # tactip_tip_to_body (fixed)
                0.00,  # tcp_joint           (fixed)
            ]
        )
    },
    "franka_panda": {
        "standard": np.array(
            [
                0.00,  # world_joint         (fixed)
                3.21456,  # panda_joint1     (revolute)
                1.30233,  # panda_joint2     (revolute)
                2.99673,  # panda_joint3     (revolute)
                0.83832,  # panda_joint4     (revolute)
                -2.97647,  # panda_joint5    (revolute)
                2.13176,  # panda_joint6     (revolute)
                4.65986,  # panda_joint7     (revolute)
                0.00,  # ee_joint            (fixed)
                0.00,  # tactip_ee_joint     (fixed)
                0.00,  # tactip_tip_to_body (fixed)
                0.00,  # tcp_joint           (fixed)
            ]
        )
    },
    "kuka_iiwa": {
        "standard": np.array(
            [
                0.00,  # world_joint          (fixed)
                0.27440,  # lbr_iiwa_joint_1  (revolute)
                1.20953,  # lbr_iiwa_joint_2  (revolute)
                2.66025,  # lbr_iiwa_joint_3  (revolute)
                1.26333,  # lbr_iiwa_joint_4  (revolute)
                -2.50256,  # lbr_iiwa_joint_5 (revolute)
                0.81968,  # lbr_iiwa_joint_6  (revolute)
                2.76347,  # lbr_iiwa_joint_7  (revolute)
                0.00,  # ee_joint             (fixed)
                0.00,  # tactip_ee_joint      (fixed)
                0.00,  # tactip_tip_to_body  (fixed)
                0.00,  # tcp_joint            (fixed)
            ]
        )
    },
}
