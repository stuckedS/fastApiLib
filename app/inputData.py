from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Address, Action, Organisation, OrganizationActions

def input():
    db: Session = SessionLocal()

    def get_or_create_address(db: Session, address_str: str, coordinates: str):
        existing_address = db.query(Address).filter(Address.address == address_str).first()
        if existing_address:
            return existing_address
        new_address = Address(address=address_str, coordinates=coordinates)
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
        return new_address

    def get_or_create_action(db: Session, action_name: str, parent_id: int = None):
        existing_action = db.query(Action).filter(Action.name == action_name).first()
        if existing_action:
            return existing_action
        new_action = Action(name=action_name, parent_id=parent_id)
        db.add(new_action)
        db.commit()
        db.refresh(new_action)
        return new_action

    address1 = get_or_create_address(db, "ул. Ленина, 10", "55.7558, 37.6173")
    address2 = get_or_create_address(db, "пр. Независимости, 20", "53.9006, 27.5590")
    address3 = get_or_create_address(db, "ул. Промышленная, 5", "55.7990, 37.6545")
    address4 = get_or_create_address(db, "ул. Гагарина, 30", "55.7350, 37.5578")
    address5 = get_or_create_address(db, "ул. Шевченко, 40", "53.8850, 27.5925")

    action_root = get_or_create_action(db, "Производственный процесс")

    action_making_meat = get_or_create_action(db, "Производство мяса", parent_id=action_root.id)
    action_quality_control = get_or_create_action(db, "Контроль качества", parent_id=action_root.id)
    action_automotive_repair = get_or_create_action(db, "Ремонт автомобилей", parent_id=action_root.id)

    action_cutting = get_or_create_action(db, "Разделка мяса", parent_id=action_making_meat.id)
    action_packaging = get_or_create_action(db, "Упаковка мяса", parent_id=action_making_meat.id)

    action_test_quality = get_or_create_action(db, "Тестирование качества", parent_id=action_quality_control.id)
    action_safety_checks = get_or_create_action(db, "Проверка безопасности", parent_id=action_quality_control.id)

    action_diagnostic = get_or_create_action(db, "Диагностика", parent_id=action_automotive_repair.id)
    action_engine_repair = get_or_create_action(db, "Ремонт двигателя", parent_id=action_automotive_repair.id)
    action_painting = get_or_create_action(db, "Покраска", parent_id=action_automotive_repair.id)

    org1 = Organisation(name="Мясокомбинат №1", telephone_number="1234563789", address=address1)
    org2 = Organisation(name="Автосервис PRO", telephone_number="9876524321", address=address2)
    org3 = Organisation(name="Пекарня №3", telephone_number="2345678390", address=address3)
    org4 = Organisation(name="ТехноСервис", telephone_number="3456738901", address=address4)
    org5 = Organisation(name="Завод Энергия", telephone_number="4567859012", address=address5)

    db.add_all([org1, org2, org3, org4, org5])
    db.commit()

    org_action1 = OrganizationActions(organisation_id=org1.id, action_id=action_making_meat.id)
    org_action2 = OrganizationActions(organisation_id=org2.id, action_id=action_automotive_repair.id)
    org_action3 = OrganizationActions(organisation_id=org3.id, action_id=action_quality_control.id)
    org_action4 = OrganizationActions(organisation_id=org4.id, action_id=action_automotive_repair.id)
    org_action5 = OrganizationActions(organisation_id=org5.id, action_id=action_making_meat.id)

    org_action6 = OrganizationActions(organisation_id=org1.id, action_id=action_cutting.id)
    org_action7 = OrganizationActions(organisation_id=org1.id, action_id=action_packaging.id)
    org_action8 = OrganizationActions(organisation_id=org2.id, action_id=action_diagnostic.id)
    org_action9 = OrganizationActions(organisation_id=org2.id, action_id=action_engine_repair.id)
    org_action10 = OrganizationActions(organisation_id=org2.id, action_id=action_painting.id)

    db.add_all([org_action1, org_action2, org_action3, org_action4, org_action5, 
                org_action6, org_action7, org_action8, org_action9, org_action10])
    db.commit()

    db.close()
    
def input2():
    db: Session = SessionLocal()

    def get_or_create_address(db: Session, address_str: str, coordinates: str):
        existing_address = db.query(Address).filter(Address.address == address_str).first()
        if existing_address:
            return existing_address
        new_address = Address(address=address_str, coordinates=coordinates)
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
        return new_address

    def get_or_create_action(db: Session, action_name: str, parent_id: int = None):
        existing_action = db.query(Action).filter(Action.name == action_name).first()
        if existing_action:
            return existing_action
        new_action = Action(name=action_name, parent_id=parent_id)
        db.add(new_action)
        db.commit()
        db.refresh(new_action)
        return new_action

    address6 = get_or_create_address(db, "ул. Невский, 15", "59.9343, 30.3351")
    address7 = get_or_create_address(db, "пр. Мира, 50", "55.7833, 49.1233")
    address8 = get_or_create_address(db, "ул. Радужная, 22", "55.0155, 82.9306")
    address9 = get_or_create_address(db, "ул. Юбилейная, 18", "55.7772, 37.6236")
    address10 = get_or_create_address(db, "ул. Советская, 12", "56.2296, 44.0975")

    action_root2 = get_or_create_action(db, "Складская логистика")

    action_inventory_management = get_or_create_action(db, "Управление инвентарем", parent_id=action_root2.id)
    action_order_processing = get_or_create_action(db, "Обработка заказов", parent_id=action_root2.id)
    action_shipment = get_or_create_action(db, "Отгрузка товаров", parent_id=action_root2.id)

    action_stock_check = get_or_create_action(db, "Проверка склада", parent_id=action_inventory_management.id)
    action_stock_replenishment = get_or_create_action(db, "Пополнение склада", parent_id=action_inventory_management.id)

    action_order_picking = get_or_create_action(db, "Сборка заказа", parent_id=action_order_processing.id)
    action_order_packaging = get_or_create_action(db, "Упаковка заказа", parent_id=action_order_processing.id)

    action_delivery = get_or_create_action(db, "Доставка товаров", parent_id=action_shipment.id)
    action_invoice = get_or_create_action(db, "Выставление счетов", parent_id=action_shipment.id)

    org6 = Organisation(name="Склад 1", telephone_number="9101234567", address=address6)
    org7 = Organisation(name="Магазин Продукты", telephone_number="9202345678", address=address7)
    org8 = Organisation(name="Грузоперевозки", telephone_number="9303456789", address=address8)
    org9 = Organisation(name="Торговая Сеть", telephone_number="9404567890", address=address9)
    org10 = Organisation(name="Логистическая Компания", telephone_number="9505678901", address=address10)

    db.add_all([org6, org7, org8, org9, org10])
    db.commit()

    org_action11 = OrganizationActions(organisation_id=org6.id, action_id=action_inventory_management.id)
    org_action12 = OrganizationActions(organisation_id=org7.id, action_id=action_order_processing.id)
    org_action13 = OrganizationActions(organisation_id=org8.id, action_id=action_shipment.id)
    org_action14 = OrganizationActions(organisation_id=org9.id, action_id=action_inventory_management.id)
    org_action15 = OrganizationActions(organisation_id=org10.id, action_id=action_order_processing.id)

    org_action16 = OrganizationActions(organisation_id=org6.id, action_id=action_stock_check.id)
    org_action17 = OrganizationActions(organisation_id=org6.id, action_id=action_stock_replenishment.id)
    org_action18 = OrganizationActions(organisation_id=org7.id, action_id=action_order_picking.id)
    org_action19 = OrganizationActions(organisation_id=org7.id, action_id=action_order_packaging.id)
    org_action20 = OrganizationActions(organisation_id=org8.id, action_id=action_delivery.id)
    org_action21 = OrganizationActions(organisation_id=org8.id, action_id=action_invoice.id)

    db.add_all([org_action11, org_action12, org_action13, org_action14, org_action15, 
                org_action16, org_action17, org_action18, org_action19, org_action20, org_action21])
    db.commit()

    db.close()

def input3():
    db: Session = SessionLocal()

    def get_or_create_address(db: Session, address_str: str, coordinates: str):
        existing_address = db.query(Address).filter(Address.address == address_str).first()
        if existing_address:
            return existing_address
        new_address = Address(address=address_str, coordinates=coordinates)
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
        return new_address

    def get_or_create_action(db: Session, action_name: str, parent_id: int = None):
        existing_action = db.query(Action).filter(Action.name == action_name).first()
        if existing_action:
            return existing_action
        new_action = Action(name=action_name, parent_id=parent_id)
        db.add(new_action)
        db.commit()
        db.refresh(new_action)
        return new_action

    address1 = get_or_create_address(db, "ул. Ленина, 10", "55.7558, 37.6173")
    address2 = get_or_create_address(db, "ул. Ленина, 15", "55.7559, 37.6174")
    address3 = get_or_create_address(db, "пр. Мира, 100", "55.7556, 37.6180")
    address4 = get_or_create_address(db, "ул. Советская, 20", "55.7550, 37.6165")
    address5 = get_or_create_address(db, "ул. Октябрьская, 5", "55.7560, 37.6176")

    action_inventory_management = get_or_create_action(db, "Управление инвентарем")
    action_order_processing = get_or_create_action(db, "Обработка заказов")
    action_shipment = get_or_create_action(db, "Отгрузка товаров")

    action_stock_check = get_or_create_action(db, "Проверка склада", parent_id=action_inventory_management.id)
    action_stock_replenishment = get_or_create_action(db, "Пополнение склада", parent_id=action_inventory_management.id)

    action_order_picking = get_or_create_action(db, "Сборка заказа", parent_id=action_order_processing.id)
    action_order_packaging = get_or_create_action(db, "Упаковка заказа", parent_id=action_order_processing.id)

    action_delivery = get_or_create_action(db, "Доставка товаров", parent_id=action_shipment.id)
    action_invoice = get_or_create_action(db, "Выставление счетов", parent_id=action_shipment.id)

    org1 = Organisation(name="Компания 1", telephone_number="9100000000", address=address1)
    org2 = Organisation(name="Компания 2", telephone_number="9200000000", address=address1)
    org3 = Organisation(name="Компания 3", telephone_number="9300000000", address=address2)
    org4 = Organisation(name="Компания 4", telephone_number="9400000000", address=address3)
    org5 = Organisation(name="Компания 5", telephone_number="9500000000", address=address4)

    db.add_all([org1, org2, org3, org4, org5])
    db.commit()

    org_action1 = OrganizationActions(organisation_id=org1.id, action_id=action_inventory_management.id)
    org_action2 = OrganizationActions(organisation_id=org2.id, action_id=action_order_processing.id)
    org_action3 = OrganizationActions(organisation_id=org3.id, action_id=action_shipment.id)
    org_action4 = OrganizationActions(organisation_id=org4.id, action_id=action_stock_check.id)
    org_action5 = OrganizationActions(organisation_id=org5.id, action_id=action_stock_replenishment.id)

    org_action6 = OrganizationActions(organisation_id=org1.id, action_id=action_stock_check.id)
    org_action7 = OrganizationActions(organisation_id=org2.id, action_id=action_order_picking.id)
    org_action8 = OrganizationActions(organisation_id=org3.id, action_id=action_order_packaging.id)
    org_action9 = OrganizationActions(organisation_id=org4.id, action_id=action_delivery.id)
    org_action10 = OrganizationActions(organisation_id=org5.id, action_id=action_invoice.id)

    db.add_all([org_action1, org_action2, org_action3, org_action4, org_action5, 
                org_action6, org_action7, org_action8, org_action9, org_action10])
    db.commit()

    db.close()
