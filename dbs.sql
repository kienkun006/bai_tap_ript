/*USE db_blackduck;
-- 1 Bảng hoKhau
CREATE TABLE hoKhau (
    id_hoKhau CHAR(9) PRIMARY KEY,
    id_cccd CHAR(12),
    chuHo VARCHAR(225),
    mqhChuHo VARCHAR(225),
    soNhanKhau INT,
    diaChi VARCHAR(225),
    ngayCap DATE,
    CHECK (id_hoKhau REGEXP '^[0-9]{9}$')
);
-- 2 Bảng congdan
CREATE TABLE congdan (
    id_cccd CHAR(12) PRIMARY KEY,
    id_hoKhau CHAR(9),
    hoVaTen VARCHAR(225),
    dob DATE,
    gioiTinh ENUM('Nam', 'Nữ'),
    TonGiao VARCHAR(225),
    danToc VARCHAR(225),
    quocTich VARCHAR(225),
    noiThuongTru VARCHAR(225),
    sinhTracHoc TEXT,
    avatar TEXT,
    CHECK (id_hoKhau REGEXP '^[0-9]{9}$'),
    FOREIGN KEY (id_hoKhau) REFERENCES hoKhau(id_hoKhau)
);
-- 3 Bảng bhyt
CREATE TABLE bhyt (
    id_bhyt CHAR(9) PRIMARY KEY,
    id_cccd CHAR(12),
    start_date DATE,
    end_date DATE,
    diaChi_dk VARCHAR(225),
    lichSu TEXT,
    CHECK (id_bhyt REGEXP '^[0-9]{9}$'),
    FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd)
);
-- 4 Bảng cuTru
CREATE TABLE cuTru (
    id_tttv CHAR(5) PRIMARY KEY,
    id_cccd CHAR(12),
    diaChi VARCHAR(225) NOT NULL,
    loai ENUM('Thường trú' ,'Tạm trú','Tạm vắng'),
    thoiHan INT,
    start_date DATE,
    end_date DATE,
    CHECK (id_tttv REGEXP '^[0-9]{5}$'),
    FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd)
);
-- 5 Bảng lichsucutru
CREATE TABLE lichsucutru (
    id_tttv CHAR(5),
    id_cccd CHAR(12),
    diaChi VARCHAR(225),
    loai ENUM('Thường trú' ,'Tạm trú','Tạm vắng'),
    start_date DATE,
    end_date DATE,
    note TEXT,
    PRIMARY KEY (id_tttv, id_cccd),
    FOREIGN KEY (id_tttv) REFERENCES cuTru(id_tttv),
    FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd)
);
alter table hokhau
add FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd)

-- 6. Bảng sự kiện
CREATE TABLE sukien (
    id_suKienPL CHAR(5) PRIMARY KEY,
    tensk VARCHAR(225),
    loai ENUM("Tạm trú","Tạm vắng","Khai sinh","Khai tử","Gia hạn BHYT","Cấp lại giấy tờ"),
    noiDung TEXT,
    CHECK (id_suKienPL REGEXP '^[0-9]{5}$')
);

-- 7. Bảng người dùng
CREATE TABLE users (
    id_user CHAR(5) PRIMARY KEY,
    id_cccd CHAR(12),
    userName VARCHAR(225),
    passWord VARCHAR(20),
    vaiTro ENUM("Công dân","Quản lý"),
    avata TEXT,
    created_at DATE,
    update_at DATE,
    CHECK (id_user REGEXP '^[0-9]{5}$'),
    FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd)
);
-- 8.Nhân khẩu
    CREATE TABLE `nhankhau` (
  `id_hoKhau` char(9) NOT NULL,
  `id_cccd` char(12) NOT NULL,
  `mqhChuHo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_hoKhau`,`id_cccd`),
  UNIQUE KEY `id_cccd_UNIQUE` (`id_cccd`),
  CONSTRAINT `nhankhau_ibfk_1` FOREIGN KEY (`id_hoKhau`) REFERENCES `hokhau` (`id_hoKhau`),
  CONSTRAINT `nhankhau_ibfk_2` FOREIGN KEY (`id_cccd`) REFERENCES `congdan` (`id_cccd`),
  CONSTRAINT `chk_nk_id_cccd` CHECK (regexp_like(`id_cccd`,_utf8mb4'^[0-9]{12}$')),
  CONSTRAINT `chk_nk_id_hoKhau` CHECK (regexp_like(`id_hoKhau`,_utf8mb4'^[0-9]{9}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- 9. Phiếu đăng ký sự kiện
CREATE TABLE phieu_dangky (
    id_phieu CHAR(5) PRIMARY KEY,
    id_cccd CHAR(12),
    id_suKienPL CHAR(5),
    loai ENUM("Tạm trú","Tạm vắng","Khai sinh","Khai tử","Gia hạn BHYT","Cấp lại giấy tờ"),
    ngayDK DATE,
    trangThai ENUM("Chưa Xử Lý","Đã Xử Lý"),
    noiDung TEXT,
    CHECK (id_phieu REGEXP '^[0-9]{5}$'),
    FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd),
    FOREIGN KEY (id_suKienPL) REFERENCES sukien(id_suKienPL)
);

-- 10. Xử lý hành chính
CREATE TABLE hanhchinh (
    id_hanhchinh CHAR(5) PRIMARY KEY,
    id_cccd CHAR(12),
    id_suKienPL CHAR(5),
    thoiGian DATETIME,
    CHECK (id_hanhchinh REGEXP '^[0-9]{5}$'),
    FOREIGN KEY (id_cccd) REFERENCES congdan(id_cccd),
    FOREIGN KEY (id_suKienPL) REFERENCES sukien(id_suKienPL)
);

-- 11. Đơn vị quản lý
CREATE TABLE dvql (
    id_dvql CHAR(5) PRIMARY KEY,
    id_hanhchinh CHAR(5),
    tendv VARCHAR(225),
    diaChi VARCHAR(225),
    CHECK (id_dvql REGEXP '^[0-9]{5}$'),
    FOREIGN KEY (id_hanhchinh) REFERENCES hanhchinh(id_hanhchinh)
);

-- 12. Tài khoản quản trị viên
CREATE TABLE admin_acc (
    id_admin CHAR(5) PRIMARY KEY,
    id_dvql CHAR(5),
    name VARCHAR(225),
    password VARCHAR(20),
    quyenHan VARCHAR(225),
    avatar TEXT,
    last_login DATETIME,
    CHECK (id_admin REGEXP '^[0-9]{5}$'),
    FOREIGN KEY (id_dvql) REFERENCES dvql(id_dvql)
);

;*/
